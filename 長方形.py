n = int(input())
if (n>0):
    for firstln in range (0,n):
        print("*",end="")
    print()
    for side in range(2,n):
        print("*",end="")
        for line in range (2,n):
            print(" ",end="")
        print("*")
    for lastln in range (0,n):
        print("*",end="")
    
        