str1=input("enter the string")
str2=str1.lower()
vowel=0
spcae=0
con=0
c=vowel+spcae+con
for i in str2:
    if i in 'aeiouAEIOU':
        vowel=vowel+1
    elif i==" ":
        spcae=spcae+1
    else:
        con=con+1
print(vowel)
print(spcae)
print(con)
