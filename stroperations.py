class Operation:
	def _init(self,string):
		self.string1=string1
	def length(self,string):
		return len(string)
	def last(self,string):
		return string[-1]
	def rep(self,string):
		return string*2
s=Operation()
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
