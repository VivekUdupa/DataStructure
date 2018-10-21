#---------------------------------------------------------#
#---- MATH 8650 Advanced Data Structures Fall 2018--------#		
#-----------Midterm Exam -- Oct 21 2018-------------------#
#----Programming Part: Implementation of Hash Table-------#
#-------------Author: Vivek Koodli Udupa------------------#
#---------------------------------------------------------#

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

		#Check if that hash entry is empty
		#If hash entry is not empty then
		if self.items[index] != None:
			
			#Extract the location into which new element will be entered replacing the old
			k1, v1, loc1 = self.items[index]

			#Replace the old key, value pair with new key,value pair
			self.array[loc1] = (k, v)

			#Update the hash table
			self.items[index] = (k, v, loc1)

		else:
			#Add elements into the auxilary array
			self.array.append( (k, v) )

			#location of the entry in auxilary array
			loc = len(self.array) - 1
		
			#Add key, value pair to items
			self.items[index] = (k, v, loc)
		
		
	def delete(self, k):
		""" Remove an object with key k """
		#Compute the hash key
		index = self.hash(k)

		#extract key value and location 
		k, v, loc = self.items[index]
		
		#Delete entry from auxilary array
		self.array[loc] = self.array[-1]
		self.array.pop(-1)
		
		#Update the hash table with new location for last entry element in array
		self.update(loc)

		print("Deleting entry: ", k, v, "\n");
		
		if( self.items[index] != None):
			#Delete the element in the key index
			self.items[index] = None
		else:
			raise KeyError(": No element found in given key:" )
			

	def update(self, loc):
		""" Updates the hash table after deletion"""
		#Extract key, value and location of updated element from array
		k, v = self.array[loc]
		
		#Find the index of the updated element
		index = self.hash(k)
		
		#Update hash table with new location
		self.items[index] = (k, v, loc)

	def find(self, k):
		""" look for entry with given key """
		#Compute the hash key
		index = self.hash(k)

		if(self.items[index] != None):
			#Print the value in the current entry
			k, v, loc = self.items[index]
			print("Found", k, v)
		
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

	def size(array):
		"""returns the size of an array"""
		return len(array)
	

#Test cases to check the working of the hash table
#Main 
h = HashTable(10)

print("\nAdding 10-Digit phone numbers and names into the list \n")
#Inserting into the Hash Table
h.insert( 8648439651, "Vivek" )
h.insert( 8646439972, "Himanshu" )
h.insert( 8646439863, "Sourabh" )
h.insert( 8646439984, "Akshay" )

#Printing the table
h.list()

print("Finding entry \'Vivek\'")
#Finding an element using its key
h.find(8646439651)

print("\nDeleting entry \'Vivek\'")
#Deleting an entry
h.delete(8646439651)

#Printing after Deletion
h.list()

print("Adding entry Shubham with the same phone-number as Himanshu \n")
#Adding element with the same key
h.insert(8646439972, "Shubham")

#Printing after insertion
h.list()
