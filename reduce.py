list=input("enter the elements").split()
print(list)
list1=map(int,list)
result=filter(lambda x:x>5,list1)
print(result)

