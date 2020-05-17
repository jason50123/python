n = int(input("請輸入大樓層數:"))
print("本大樓具有的樓層數為:",end="")
if n > 3 :
    n+=1
for i in range(1,n+1):
    if i == 4:
        continue
    print (i,end=" ")