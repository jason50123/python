n = input()
n = int(n) 
if (n>0):
    for i in range (0,n):
        print("*",end="")
    print()
    for j in range(2,n):
        print("*",end="")
        for k in range(2,n):
            print(" ",end="")
        print("*")
    for m in range(0,n):
        print("*",end="")
        