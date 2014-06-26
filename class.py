class Calculator1:
	def __init__(self, x, y):
		self.__x = x
		self.x = x
		self.y = y
	def add(self):
		return self.x+self.y
	def sub(self):
		return self.x - self.y
	def mul(self):
		return self.x*self.y
	def div(self):
		return self.x/self.y
	def add2num(self, x, y):
		return self.x + self.y + x + y

class Calculator2:
	def __init__(self):
		print ("Initialized calculator engine")
	def add(self, x, y):
		return x+y
	def sub(self, x, y):
		return x - y
	def mul(self, x, y):
		return x*y
	def div(self, x, y):
		return x/y
		
if __name__ == "__main__":
	c = Calculator2()
	print ("choose an operation:")
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
