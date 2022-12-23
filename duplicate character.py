
string="Python programming"
duplicate=[]
c=0
for i in string:
    if string.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
            c=c+1
print(duplicate)
print(c)