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
	#Initialize a Temporary stack for reversal
	T = Stack()
	
	#Get the size of the Sinal stack
	n = r.size()

	#variable to store count
	count = 0
	while(count < n-1):
		#switch contents of r and T
		r, T, v = switch1(n, r, T)
		"""	
		print("after switch1, count is: ", count)
		print("Sinal is: ", end = " ")
		r.show()
		print("\n Torary is: ", end = " ")
		T.show()
		print("\n v = ", v)
		"""
		#switch contents back to r from T
		r, T = switch2(n, count, r , T, v)
		"""	
		print("after switch2, count is: ", count)
		print("Sinal is: ", end = " ")
		r.show()
		print("\n Torary is: ", end = " ")
		T.show()
		print("\n v = ", v)
		"""
		count = count + 1

	return r

def switch1(n, S, T):
	"""Switch 1 """
	
	for sc in range(n): 
		
		#Store first iT in auxilary variable
		if(sc == 0):
			v = S.pop()
		
		#store rest of the items in Torary stack
		else:
			T.push(S.pop())
		
	return S, T, v

def switch2(n, count, S, T, v):
	"""Switch 2 """
	
	for sc in range(n):
		#Reordering using the auxilary variable 
		if(sc == count):
			S.push(v)

		#Push normally into Sinal from T
		else:
			S.push( T.pop() ) 

	return S, T

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
