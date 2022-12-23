str1='i love Aamy'
c=0
for i in str1:
    if i in 'aeiouAEIOU':
        c+=1
print("count of vowels is",c)
print(str1.count('A'))
print(len(str1))
print(str1.replace('Aamy','Nimmi'))
print(str1.find('Aamy'))

