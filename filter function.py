#lst=[1,2,3,4]
#result=filter(lambda x:x%2==0,lst)
#print(list(result))

lst=input("enter the element").split( )
print(lst)
lst1=map(int,lst)
even=filter(lambda x:x%2==0,lst1)
print(list(even))
