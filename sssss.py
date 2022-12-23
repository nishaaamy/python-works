def printer(name):
    global count
    if count<=10:
        print(name)
        count+=1
        printer("nisha")