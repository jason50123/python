n = input()
n = int(n)
if (n>=1 and n<=20):
    for i in range (1,n+1):
        for j in range(0,i):
            print('*',end="")
        print()        