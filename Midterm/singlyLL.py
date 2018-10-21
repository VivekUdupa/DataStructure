class Node :
	"""Node class"""

	def __init__(self, data = None, next = None):
		"""Initializing Parameters"""
		self.data = data
		self.next = next

	def getNextNode(self):
		"""Returns the Next Node"""
		return self.next

	def setNextNode(self, newNext):
		"""Sets the current node pointer to next node"""
		self.next = newNext

	def getData(self):
		"""Returns the Current Node Data"""
		return self.data

class LinkedList():
	"""Single Linked List"""

	def __init__(self):
		"""Initializing Parameters"""
		self.head = None
		
	def push(self, data):
		"""Pushest elements to the begining of the list"""
		newNode = Node(data) #Initialize new node with the given data
		newNode.setNextNode(self.head)	#set the next node to the head of the node  
		self.head = newNode #Set the head to the new created node

	def printLis(self):
		"""Prints the entire list"""
		current = self.head
		while current :
			print(current.data," ",end="")
			current = current.getNextNode()
		print()

	def deleteEven(self, prev = None, current = None):
		"""To delete all even numbers from the list recursively"""
		#If entering for the first time, set parameters to point at head and first node
		if(prev == None and current == None):
			prev = None
			current = self.head

		#Return if we recursed to the end
		if current == None:
			#print("Reached the end")
			return
		
		#If not the end, the delete even numbers
		elif (current.data % 2 == 0):
			#print("deleting: ",current.data)
			
			#Point the previous to the next element so that the even number is skipped
			if(prev == None):
				self.head = current.getNextNode()
				prev = self.head
			else:
				prev.setNextNode(current.getNextNode())

			#Check if we are at the last node
			if(current.getNextNode() == None) :
				current = None
			else:
				current = current.getNextNode()
		
		else:
			prev = current
			current = current.getNextNode()

		self.deleteEven(prev,current)

lis = LinkedList() 

i = 20
#Push i elements into the linked list
while i>=0:
	lis.push(i)
	i = i - 1

print("List is: ")
lis.printLis();

#Delete even numbers
lis.deleteEven();			

print("After removing even entries")
lis.printLis();

