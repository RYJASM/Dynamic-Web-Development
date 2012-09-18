# This is fake data structure for my theoretical class review system

Dynamic_Web_Development={
	'name':'Dynamic Web Development',
	'professor':'J.Schimmel',
	'term':'Fall',
	'year':2012,
	'capacity':16,
	'website':'http://itppyweb.herokuapp.com/',
	'id':00001
}

Understanding_Networks={
	'name':'Understanding Networks',
	'professor':'T.igoe',
	'term':'Fall',
	'year':2012,
	'capacity':16,
	'website':'http://itp.nyu.edu/understandingnetworks/',
	'id':00002
}


Printing_Code={
	'name':'Printing Code',
	'professor':'R.Madsen',
	'term':'Fall',
	'year':2012,
	'capacity':16,
	'website':'http://www.runemadsen.com/printing-code-2012',
	'id':00003
}

Visualizing_JS={
	'name':'Visualizing JS',
	'professor':'S.Smith',
	'term':'Fall',
	'year':2012,
	'capacity':16,
	'website':'http://stewd.io/javascript/index.html',
	'id':00004
}

MakeMatics={
	'name':'MakeMatics',
	'professor':'G.Borenstein',
	'term':'Fall',
	'year':2012,
	'capacity':16,
	'website':'http://makematics.com/syllabus/2012-Fall/',
	'id':00005
}


Review={
	'coursename':'Dynamic Web Development',
	'year': 2013,
	'id':000001,
	'review_date':'2012-09-15',
	'review_comment':'This class is amazing, and needs to be offered every semester...',
	'reviewusefulnessindex':3 
}

Reviewer={
	'name':'mark breneman',#this could be optional
	'course_name':'Dynamic Web Development',
	'year': 2013,
	'coursework_link':'www.markbreneman.com/blog',
	'previous_courses': ['PComp', 'Comm.Lab Web', 'Comm.Lab Video and Sound', 'ICM', 'Comm.Lab 2D-Design','HTML5','Nature of Code', 'Wildlife Tools', 'Designing Conversational Spaces'],
	'id':0001
}




#Create a list of dictionaries
print "*" *75 
Classlist=[Dynamic_Web_Development, Understanding_Networks, Printing_Code, Visualizing_JS, MakeMatics]

#Loop though list and print out data
print "*" *75 
for classes in Classlist:
	print classes.get('name'), 'is taught by', classes.get('professor'), 'in the', classes.get('term'),  classes.get('year'), 'and has a website at %s' % classes.get('website')

#Create a class for the objects
print "*" *75 
class classobject(object):
	
	# __init__ automatically called when creating an object
	def __init__(self, data=None): #none is a datatype
		print "Creating new class:", data.get('name')
		self.name = data.get('name')
		self.professor = data.get('professor')
		self.term = data.get('term')
		self.year = data.get('year')
	

#Create a class for the reviews
print "*" *75 
class reviewobject(object):

	# __init__ automatically called when creating an object
	def __init__(self, review=None): #none is a datatype
		print "Creating new review:", review.get('coursename')
		self.name = review.get('coursename')
		self.year = review.get('year')
		self.date = review.get('review_date')
		self.comment = review.get('review_comment')	
		self.usefulness = review.get('reviewusefulnessindex')
		
	
#create an object using the class
classobject(Dynamic_Web_Development)
print "*" *75 
reviewobject(Review)



# Create a list of the objects
print "*" *75 
classobjectlist=[]		
for classes in Classlist:
	classobjectlist.append( classobject(classes) )
# 
#Print the list of class objects weight
for classobject in classobjectlist: 
	print "*" *75 
	print classobject.name
	print classobject.professor
	print classobject.term
	print classobject.year
# print "*" *75 
# for classobject in classobjectlist: 
# 	print "*" *75 
# 	print classobject


	





