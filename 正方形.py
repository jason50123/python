n =input()
n = int(n)
if (n>=1 and n<=20):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            j+=1
        i+=1
        print()