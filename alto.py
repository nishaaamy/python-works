n=int(input("enter the number"))
sum=0
num=n
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10
print(sum)
if(sum==num):
    print("is amstrong numberr")
else:
    print("not amstrong number")