list1=[1,3,4,2,1,5,4,6]
result=[ ]
for i in list1:
    if list1.count(i)>1:
        result.append(i)
print(result)