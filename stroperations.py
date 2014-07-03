class Operation:
    # aseem: please read the documentation of classes again.
    # Q: When you define a class (for example in c++= and give
    # some arguments in the constructor, how do you instantiate
    # the class?
	def _init(self,string):
        # When you initially defined the object, what was the purpose
        # of defining the __init__ ?
        # Why did you define the init as def __init__(self, string): ?
        # What is the purpose of the argument string?
		self.string1=string1
	def length(self,string):
		return len(string)
	def last(self,string):
		return string[-1]
	def rep(self,string):
		return string*2
s=Operation()
# In your current class definition, there is no constructor and so,
# this works. What change you should do to initialize this object?
print("choose an operation:")
print("1:length of string:")
print("2:concatenation of string:")
print("3:last char of string1:")
print("4:repetition of string1:")
choice=input("enter the choice:")
string=input("enter the string:")
if choice=='1':
	print("length of string is",s.length(string))
elif choice=='2':
	print("last char of string is",s.last(string))
elif choice=='3':
	print("repetition of string1 is",s.rep(string))
else:
	print("error")
