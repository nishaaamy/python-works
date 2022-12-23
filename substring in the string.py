str1=input("enter the string")
sub=input("enter the substring")
r=str1.find(sub)
if(r!=1):
    print("The substring is in the string",r)
else:
    print("the substring is not in the string ")