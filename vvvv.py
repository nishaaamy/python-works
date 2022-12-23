list="b,b,b,b,z,z,z,z,z,a,a"
list2=list.split(',')
visitedlist=[]
for i in list2:
    if i not in visitedlist:
        print(f"{i}:{list2.count(i)}",end=",")
        visitedlist.append(i)