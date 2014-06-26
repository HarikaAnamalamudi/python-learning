print ("Choose an operation:")
print ("1.+")
print ("2.-")
print ("3.*")
print ("4./")

choice =input ("enter choice")
num1= int(input("enter the first operand:"))
num2= int(input("enter the second operand:"))

if choice=='1':
	print(num1,"+",num2,"=", num1+num2)
elif choice=='2':
	print(num1,"-",num2,"=", num1-num2)
elif choice=='3':
	print(num1,"*",num2,"=", num1*num2)
elif choice=='4':
	print(num1,"/",num2,"=", num1/num2)
else:
	print("error!operator not correct.")
