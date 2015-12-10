""""A queue ADT for python 3.x.
by Jordan Ogilvy
"""
#The queue ADT has the following methods, which each have a description of what they do in the Queue class:
#enqueue(item)
#dequeue()
#peek()
#size()
#is_empty()

class Queue:
	def __init__(self):
		self.__queue = [] #implement the queue with a python list which will hold the queued items
		self.__front = 0 #index of the item at the front of the queue 
		self.__back = 0 #index the NEXT queued item will go into 
		self.__length = 0 #number of items in the queue
		
	def enqueue(self, item):
		#add the passed item to the back of the queue. Update the location of the back of the queue.
		#there is a special case for when the queue is empty.		
		if self.is_empty():
			self.__back = 0   #move the front and back positions to the front of the python list
			self.__front = 0
			self.__queue = [] #recreate the python list, removing all the None elements, to save memory
			
		try:
			self.__queue[self.__back] = item	
		except IndexError:
			self.__queue.append(item) #add the item to the queue
		
		self.__back = self.__back + 1
		self.__length = self.__length + 1
	
	def dequeue(self):
		#Remove and return the item at the front of the queue.
		#If the queue is already empty, return None and a error message without terminating
		if self.is_empty():
			print("Queue is empty: cannot dequeue")
			return
		else:
			front_item = self.__queue[self.__front]
			self.__queue[self.__front] = None
			self.__front = self.__front + 1
			self.__length = self.__length - 1
			return front_item
	
	def peek(self):
		#return the item at the front of the queue, without removing/dequeuing it.
		if self.is_empty():
			return
		else:
			return self.__queue[self.__front]
	
	def size(self):	
		#return the size of the queue
		return self.__length
		
	def is_empty(self):
		#returns True if the queue is empty (has no items queued), returns False if not
		return self.__length == 0
		
	def __repr__(self):
	
		#show the queue as a slice of the list, with the front item on the left/front, and the back item at the end.
		#e.g. "[front_item, ..., ..., ..., back_item]"
		return str(self.__queue[self.__front:self.__back])
	
	def __len__(self):
		return self.size()
		
	def __contains__(self, other):
		#return True if the passed item, other, is in the queue
		return other in self.__queue[self.__front:self.__back]

		queue_copy = Queue()
		for item in self.__queue[self.__front:self.__back]:
			queue_copy.enqueue(item)
			
		return queue_copy
