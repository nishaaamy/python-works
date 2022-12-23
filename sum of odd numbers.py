li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
oddlist=[]
s=0
for i in li:
    if(i%2!=0):
        oddlist.append(i)
        s=s+i
print(oddlist)
print(s)