print("This program reverses a string:")
string=input("enter the string:")
if len(string)<=1:
	print("string")
else:
	print("reverse string is:",reverse(string[1:])+string[0])
