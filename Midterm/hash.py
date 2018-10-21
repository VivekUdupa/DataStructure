class HashTable():
	"""Hash table for storing phone numbers"""

	def __init__(self, n=1000):
		"""Iniitalize the hash table"""
		self.capacity = n
		self.size = 0
		self.items = [None] * self.capacity
		self.array = []
		 
	def hash(self, key):
		"""Generates hash key"""
		index = (key % self.capacity)
		return index

	def insert(self, k, v):
		""" insert key value pair into the hash table """
		#increment the size
		self.size += 1

		#Compute hash key
		index = self.hash(k)

		#Add key, value pair to items
		self.items[index] = (k, v)
		
		#Add elements into the auxilary array
		self.array.append( (k, v) )
		
	def delete(self, k):
		""" Remove an object with key k """
		#Compute the hash key
		index = self.hash(k)
		
		#extract key value pair 
		key, value = self.items[index]
		
		if( self.items[index] != None):
			#Delete the element in the key index
			self.items[index] = None
		else:
			raise KeyError(": No element found in given key:" )
			
		#Deleting from auxilary array
		m = len(self.array) 
		i = 0

		while(i < m):
			if(self.array[i] == (key, value)):
				self.array.pop(i)
				return
			i += 1

	def find(self, k):
		""" look for entry with given key """
		#Compute the hash key
		index = self.hash(k)

		if(self.items[index] != None):
			#Print the value in the current entry
			key, value = self.items[index]
		
		else:
			raise KeyError("No element found in given key")
			

	def list(self):
		""" Display the hash table """
		
		print("---------------Phonebook------------------")
		print("Phone-Number", "\t \t", "Name")
		print("------------", "\t \t", "-----------")
		#Print using auxilary array
		for i in range(len(self.array)):
			num, name = self.array[i]
			print(num, "\t \t", name)
	

	#	for item in self.items:
	#		if item is not None:
	#			print(str(item))
	#	print()


h = HashTable(10)

h.insert( 8648439651, "vivek" )
h.insert( 8646439972, "himanshu" )
h.insert( 8646439863, "chakan" )
h.insert( 1234567898, "sadhu" )
h.list()

h.find(8646439651)
h.delete(1234567898)

h.list()
