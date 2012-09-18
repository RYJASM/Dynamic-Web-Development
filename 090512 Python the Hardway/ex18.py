# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is acutally pointless, we can just to this

def print_two_again(arg1,arg2):
	print "arg1: %r, arg2 %r" % (arg1, arg2)
	
#this just takes on argument
def print_one(arg1):
	print "arg1: %r" % arg1	
	
#this one takes no agruments
def print_none():
	print "I got nothin'."
	
print_two("mark", "breneman")
print_two_again("mark", "breneman")
print_one("First!")
print_none()