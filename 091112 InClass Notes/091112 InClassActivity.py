# Create five dictionaries: in this case Candy
Cadbury={
	'name':'cadbury',
	'weight': 3.5,
	'type':'milk chocolate',
	'color':'purple'
}

Twix={
	'name':'Twix',
	'weight': 3.02,
	'type':'caramel',
	'color':'gold'
}

Butterfinger={
	'name':'Butterfinger',
	'weight': 3.7,
	'type':'peanut butter',
	'color':'yellow'
}

MandM={
	'name':'M&M',
	'weight': 1.08,
	'type':'peanut',
	'color':'brown','yellow','blue'
}

Lindt={
	'name':'Lindt',
	'weight': 3.5,
	'type':'dark chocolate',
	'color':'beige'
}

#Create a list of dictionaries
# print "*" *75 
Candylist=[Cadbury,Twix,Butterfinger,MandM,Lindt]

#Loop though list and print out data
# print "*" *75 
#for candy in Candylist:
	# print candy.get('name'), 'weighs', candy.get('weight'), 'is of type', candy.get('type'), 'and is in %s' % candy.get('color')

#Create a class for the objects
print "*" *75 
class candyobject(object):
	
	# __init__ automatically called when creating an object
	def __init__(self, data=None): #none is a datatype
		print "Creating new candybar:", data.get('name')
		self.name = data.get('name')
		self.weight = data.get('weight')
		self.type = data.get('type')
		self.color = data.get('color')
		
	
	# def set_name(self, name):
	# 		self.name = name
	# 		
	# def cheerfor(self):
	# 			return self.name + "Candybar"
	
#create an object using the class
# candyobject(Lindt)


# Create a list of the objects
candyobjectlist=[]		
for candy in Candylist:
	candyobjectlist.append( candyobject(candy) )

#Print the list of candy objects weight
for candyobject in candyobjectlist: 
	print "*" *75 
	print candyobject.name
	print candyobject.weight
	print candyobject.type
	print candyobject.color
print "*" *75 
for candyobject in candyobjectlist: 
	print "*" *75 
	print candyobject


	





