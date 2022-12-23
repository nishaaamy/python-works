list=[1,2,2,3,3,4,5,5,5,6,6]
mylist=[]
for i in list:
    if list.count(i)==1:
        mylist.append(i)
print(mylist)

list=[1,2,2,3,3,4,5,5,5,6,6]
mylist=[i for i in list if list.count(i)==1]
print(mylist)
