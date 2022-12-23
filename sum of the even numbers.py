li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evenlist=[]
s=0
for i in li:
    if(i%2==0):
        evenlist.append(i)
        s=s+i
print(evenlist)
print(s)