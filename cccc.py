#input 'abcaba'
#output abcaabbaaa

str1='abcaba'
mydict={}
for ch in str1:
    if ch not in mydict:
        mydict[ch]=1
        print(ch,end="")
    else:
        mydict[ch]=mydict[ch]+1
        print(ch*mydict[ch],end="")