def perfect(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
            if(sum==num):
                print("perfect number")
            else:
                print("not a perfect number")
perfect(7)
