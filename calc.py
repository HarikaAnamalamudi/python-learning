import sys
print("command_line_arguments_count:",len(sys.argv))
print("command_line_arguments:")
print(" ",sys.argv)


#check number of strings passed

if len(sys.argv)!=4:
	print("usage not correct")
	sys.exit()
#determine the operator

if sys.argv[2][0]=='+':
	result=eval(sys.argv[1])+eval(sys.argv[3])
elif sys.argv[2][0]=='-':
	result=eval(sys.argv[1])-eval(sys.argv[3])
elif sys.argv[2][0]=='*':
	result=eval(sys.argv[1])*eval(sys.argv[3])
elif sys.argv[2][0]=='/':
	result=eval(sys.argv[1])/eval(sys.argv[3])

#display result
print(sys.argv[1]+''+sys.argv[2]+''+sys.argv[3]+''+str(result))