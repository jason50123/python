n = int(input())
print("本大樓有的樓層:")
if n > 3 :
    n+=1
for i in range (1,n+1):
    if(i == 4):
        continue
    print(i,end = " ")
