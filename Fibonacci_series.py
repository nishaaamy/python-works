n=int(input("enter the limit"))
f=0
s=1
t=0
print(f,s,end="")
for i in range(n-2):
    t=f+s
    f=s
    s=t
    print(t,end="")



