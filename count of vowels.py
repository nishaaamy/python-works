str=input("enter the string")
c=0
for i in str:
    if i in 'aeiouAEIOU':
        c=c+1
print(c)