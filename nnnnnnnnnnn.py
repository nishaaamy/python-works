mystr="a,a,a,b,b,c,c,c"
mylist=mystr.split(',')
visited=[]
for i in mylist:
    if i not in visited:
        print(f"{i}:{mylist.count(i)}",end=",")
        visited.append(i)