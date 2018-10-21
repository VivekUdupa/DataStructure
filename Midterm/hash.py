#---------------------------------------------------------#
#---- MATH 8650 Advanced Data Structures Fall 2018--------#		
#-----------Midterm Exam -- Oct 21 2018-------------------#
#----Programming Part: Implementation of Hash Table-------#
#-------------Author: Vivek Koodli Udupa------------------#

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
		
		print("Deleting entry: ", key, value, "\n");
		
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
			print("Found", key, value)
		
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

		print("\n")
	

#Main 
h = HashTable(10)

#Inserting into the Hash Table
h.insert( 8648439651, "Vivek" )
h.insert( 8646439972, "Himanshu" )
h.insert( 8646439863, "Sourabh" )
h.insert( 8646439984, "Akshay" )

#Printing the table
h.list()

#Finding an element using its key
h.find(8646439651)

#Deleting an entry
h.delete(8646439651)

#Printing after Deletion
h.list()

#Adding element with the same key
h.insert(8646439972, "Shubham")

#Printing after insertion
h.list()
