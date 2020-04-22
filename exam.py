n = input()
n = int(n)
if(n>=1 and n<=20):
    for i in range(1,n+1):
        for j in range(1,i):
            print(' ',end="")
        for k in range (n+1,i,-1):
            print("*",end="")
        print()
