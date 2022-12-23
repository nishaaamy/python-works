num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
ch=int(input("enter your choice"))
if(ch==1):
    result=num1+num2
    print(result)
elif(ch==2):
    result=num1-num2
    print(result)

elif(ch==3):
    result=num1*num2
    print(result)

elif(ch==4):
    result=num1/num2
else:
    print("wrong choice")

