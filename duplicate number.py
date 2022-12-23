li=[1,2,3,1,4,5,6,3,7,8,9,10,2,3,6,11,13,12,7,8,9]
duplicateli=[]
for i in li:
       if li.count(i)>1:
        if i not in duplicateli:
           duplicateli.append(i)
print(duplicateli)