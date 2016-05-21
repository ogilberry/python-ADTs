"""A LinkedList ADT for python
By Jordan Ogilvy
"""
#The Linked List consists of Nodes, which contain the data/item, and a reference/link to the next
#Node. The Nodes are implemented with a class. The LinkedList is also implemented with a class,
#and uses instances of the Node class to create the list.


class Node:
	def __init__(self, item):
		self.__item = item #the actual item the node stores
		self.__next = None #the link/reference/pointer? to the next node, should be assigned a node or None
		
	#accessor methods for the item and next data fields
	def get_next(self):
		return self.__next
		
	def set_next(self, new_next):
		self.__next = new_next
		
	def get_item(self):
		return self.__item
		
	def set_item(self, new_item):
		self.__item = new_item


class LinkedList:
	#the LinkedList class keeps a reference to the first node in the list, head, and
	#implementations for the linked list methods
	def __init__(self):
		self.__head = None
		self.__size = 0
		self.__current = None
		
	def add(self, item):
		#This essentially makes the new node the head, then makes it point to the old head, which is similar to
		#inserting the new item at index 0 of a python list, and shuffling the other elements 1 indice along,
		#except this add method has complexity of O(1).
		
		new_node = Node(item) #create a node for the item
		new_node.set_next(self.__head) #make the new node point/link to the current head node
		self.__head = new_node #change the head to point to the new node
		self.__size = self.__size + 1 #increment the size
		
	def is_empty(self):
		#returns True if there are no nodes in the list (i.e it is empty), otherwise returns False
		return self.__head == None
		
	def size(self):
		#returns the number of nodes, i.e the size/length, of the linked list
		return self.__size
	
	def search(self, item):
		#searches in the linked list through every node for the specified item, returns True if 
		#it is in the linked list
		current_node = self.__head
		while current_node != None: #Loop until the end of the linked list is reached
			if current_node.get_item() == item: #check this node has the item we are searching for
				return True
			else:
				current_node = current_node.get_next() #if it doesn't, go to the next node
				
		return False #return False after every node has been searched. Has worst case O(n)
	
	def remove(self, item):
		#removes the specified item from the linked list. The node which points to the node we want to 
		#remove will now point to the node the node we want to remove points to.
		
		if self.is_empty(): #return an error without terminating if the linked list is empty
			return
		
		found = False #Boolean we will change when we find the item we want to remove
		preceding_node = None #variable for the node that points to the node we want to remove
		current_node = self.__head
		
		#loop through all the nodes in the list until the node to be removed is found
		while current_node != None and not found:
			if current_node.get_item() == item:
				found = True #if we find the node to be removed, set found to True, so we can exit the loop
			else:
				preceding_node = current_node 
				current_node = current_node.get_next() #go to the next node to check for the item
				
		if found:
			if preceding_node == None: #if the node to be removed is the head, i.e has no preceding nodes
				self.__head = current_node.get_next() #we only need to change the head to the node after it
			else:
				#change the node preceding the node to be removed so that it points to the node after it,
				#bypassing the node we are removing, so it is no longer linked to the list
				preceding_node.set_next(current_node.get_next())
			#once the node is removed, decrement the size of the linked list
			self.__size = self.__size - 1
			
		#else the item is not in the list
		else:
			return
		
	def __len__(self):
		#See size(), returns the number of nodes in the linked list.
		return self.size()
		
	def __iter__(self):
		self.__current = self.__head
		return self
		
	def __next__(self):
		if self.__current == None:
			raise StopIteration
		else:
			item = self.__current.get_item()
			self.__current = self.__current.get_next()
			return item
			
			
