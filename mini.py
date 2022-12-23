str1="i like programming"
duplicate=[]
c=0
for i in str1:
     if str1.count(i)>1:
         if i not in duplicate:
          duplicate.append(i)
                   c=c+1
print(duplicate)
print(c)