n=int(input("enter the number"))
sum=0
num=n
while(n>0):
    d=n%10
    sum=sum+d**3#0+1**3(0+1)  sum=(1+7**3)(343) 1+343+3**3(27) 1+343+27
    n=n//10
print(sum)
if(sum==num):
    print("its an amstrong number")
else:
    print("its not an amstrong number")