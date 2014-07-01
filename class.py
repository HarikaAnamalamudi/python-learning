class Calculator:
	def _init(self,x,y):
		self.x=x
		self.y=y
	
	def add(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y
	def mul(self,x,y):
		return x*y
	def div(self,x,y):
		return x/y
c = Calculator()
print ("choose an operation")
print("1.+")
print("2.-")
print("3.*")
print("4./")
choice=input("enter choice:")
num1 = int(input("enter the first operand"))
num2 = int(input("enter the second operand:"))
if choice=='1':
	print(num1,"+",num2,"=",c.add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",c.sub(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",c.mul(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",c.div(num1,num2))
else:
	print("error!operator not correct")

