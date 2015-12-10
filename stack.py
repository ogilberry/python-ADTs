"""A basic stack ADT for python, by Jordan Ogilvy"""


class stack:
	def __init__(self):
		#create the empty stack by creating an empty list. Make it accessible only by accessor functions
		self.__stack = []
		
	def push(self, item):
		#add an item to the top of the stack
		self.__stack.append(item)
		
	def pop(self):
		#copy and store the item at the top of the stack, delete it from the stack, then return the stored item
		try:
			item = self.__stack[(len(self.__stack)) - 1]
			del self.__stack[(len(self.__stack)) - 1]
			return item
		except IndexError:
			print("IndexError: The stack is empty.")
		except:
			print("An error occured when popping the stack.")
		
	def peek(self):
		#return the item at the top of the stack. Returns None if empty. 
		if self.is_empty():
			return None
		else:
			return self.__stack[(len(self.__stack)) - 1]
		
	def is_empty(self):
		#checks if the stack is empty, returns true or false
		return len(self.__stack) == 0
		
	def size(self):
		#returns number of elements in the stack
		return len(self.__stack)
		
	def __repr__(self):
		return str(self.__stack)
