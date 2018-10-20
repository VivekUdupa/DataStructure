class Stack:
	"""Implements a stack"""
	def __init__(self):
		self.items = []
	
	def push(self, data):
		"""Adds data into the leftmost position"""
		self.items.insert(0,data)
	
	def pop(self):
		"""Pops left most element"""
		return self.items.pop(0);

	def show(self):
		"""Prints the stack"""
		n = self.size()
		for i in range (n):
			print(self.items[i], " ", end = " ")
		print()

	def size(self):
		"""Returns the size of the stack"""
		return len(self.items)

#Functions
def reverse(r):
	"""Returns the reversed Stack"""
	#Initialize a temporary stack for reversal
	temp = Stack()
	
	#Get the size of the original stack
	n = r.size()

	#variable to store count
	count = 0
	while(count < n-1):
		#switch contents of r and temp
		r, temp, v = switch1(n, r, temp)
		"""	
		print("after switch1, count is: ", count)
		print("original is: ", end = " ")
		r.show()
		print("\n temporary is: ", end = " ")
		temp.show()
		print("\n v = ", v)
		"""
		#switch contents back to r from temp
		r, temp = switch2(n, count, r , temp, v)
		"""	
		print("after switch2, count is: ", count)
		print("original is: ", end = " ")
		r.show()
		print("\n temporary is: ", end = " ")
		temp.show()
		print("\n v = ", v)
		"""
		count = count + 1

	return r

def switch1(n, orig, temp):
	"""Switch 1 """
	
	for sc in range(n): 
		
		#Store first itemp in auxilary variable
		if(sc == 0):
			v = orig.pop()
		
		#store rest of the items in temporary stack
		else:
			temp.push(orig.pop())
		
	return orig, temp, v

def switch2(n, count, orig, temp, v):
	"""Switch 2 """
	
	for sc in range(n):
		#Reordering using the auxilary variable 
		if(sc == count):
			orig.push(v)

		#Push normally into original from temp
		else:
			orig.push( temp.pop() ) 

	return orig, temp

#Main
s = Stack()

#Populate the stack
for i in range (10) :
	s.push(i);

print("Before reversal")
s.show()

#Reverse the stack
s = reverse(s)

print("after reversal")
s.show()
