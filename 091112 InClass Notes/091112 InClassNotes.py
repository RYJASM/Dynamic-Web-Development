# dictionary
# mission_dates = {
# 	'Gemini 3' : '23 March 1965',
# 	'Gemini 10' : '18-21 July 1966',
# 	'Apollo 10' : '18-26 May 1969',
# 	'Apollo 16' : '16-27 April 1972 ',
# 	'STS-1' : '12-14 April 1981',
# 	'STS-9' : '28 November - 6 December 1983'
# }

# retrieve mission
# print mission_dates['Apollo 16']

# print mission_dates.get('Apollo 16')
# print mission_dates.get('Apollo 13')#returns None which is like javascripts undefined

# print mission_dates.keys() # Show all the keys of the dictionary
# print mission_dates.values() #Show up all the values in the dictionary
# print mission_dates.items() #Show all the tuples... the .items is what calls the tuples


# TUPLES
# print ""
#Loop through dictionary; show list of name and date in alphabetical order
#Tuples maintain order!
# for name, date in mission_dates.items():#loop through the dictionary show tuples
# 	print name,"on", date 


# OBJECTS

# class Astronaut(object):
# 	
# 	# __init__ automatically called when creating an object
# 	def __init__(self, nameStr = None):
# 		print "Creating new astronaut:", nameStr
# 		self.name = nameStr
# 
# 	def set_name(self, nameStr):
# 		self.name = nameStr
# 		
# me=Astronaut('mark')

####################	
#simplest class definition	
# class Dot(object):
# 	pass
# 	
# mydot=Dot()
# mydot.color = 'red'
# mydot.size = '10'
# # calling variables with comma notation
# print mydot.color, "is the color and it is", mydot.size
# # calling variable with % notation
# print "%s is the color" % mydot.color
# # calling more than one variable
# print "%s is the color and it is %s" % (mydot.color, mydot.size)
# #mydot.size should be called with %d as it is a number not a string. Python will cast is as a string
# 
# print dir(mydot)#sees all the properties of the object including defaults of python
# 
# print mydot
################################

class Astronaut(object):
	
	#properties/attributes/variables
	#describe the object
	
	# __init__ automatically called when creating an object
	def __init__(self, nameStr = None):
		print "Creating new astronaut:", nameStr
		self.name = nameStr
# 
# 	#VERB WHICH SETS ATTRIBUTES
# 	def set_name(self, nameStr):
# 		self.name = nameStr
# 
# 	#VERB for do something with this object	
# 	def cheerfor(self):
# 		return self.name + "!!!"
# 		
me=Astronaut('mark')
matt=Astronaut('matt')

# me.cheerfor()
# crew= [me,matt]

# for astro in crew:
# 	astro.cheerfor();
# 
# 

# ###List of objects rather than just names
# civilians = ['john', 'matt', 'fed']
# ###Creating a list with objects in it
# crew = []#empty list
# for c in civilians:
# 	tmpAstro = Astronaut(c) #create a new astronaut from c
# 	crew.append(tmpAstro)
# #show me the list and use length to capture objects
# print "There are", len(crew), "astronauts"
# 
# # to debug use the print * notation to show breaks in operation
# print "*" *50, "Loop through Astronauts", "*"*50
# 
# for astro in crew:
# 	print astro.cheerfor()

