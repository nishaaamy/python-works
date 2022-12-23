lst=input("enter the elements ").split()
print(lst)
lst2=map(int,lst)
result=filter(lambda x:x>5,lst2)
print(list(result))




