str1="a,a,a,a,b,b,b,c,c,d"
mystr=str1.split(',')
visited=[]
for ch in mystr:
    if ch not in visited:
        print(f"{ch}:{mystr.count(ch)}",end=",")
        visited.append(ch)

