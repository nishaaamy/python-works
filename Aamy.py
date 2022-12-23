n=int(input("enter the rows needed:"))
for row in range(n,0,-1):
    for coloumn in range(1,row+1):
        print("*",end="")
    print()