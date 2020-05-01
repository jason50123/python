n = int(input())
if (n>0 and n<200):
    fif =str(n//50) 
    n%=50
    ten = str(n//10)
    n%=10
    five =str(n//5)
    n%=5
    one = str(n)
    print("$50:"+fif+"|$10:"+ten+"|$5:"+five+"|$1:"+one)    