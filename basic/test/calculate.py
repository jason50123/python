def gcd(x1,x2):
    result = 0
    while result ==0:
        if x1 < x2 :
            x1,x2= x2,x1
            print("x1 = ", x1,"\nx2= ", x2)

        if x1 % x2 == 0:
            print("")
            result = x2
        else:
            x1 = x1 % x2
    return result

def little(x1,x2):
    result = 0
    total = 0
    while x1 % x2 !=0 | x2 % x1 !=0:
        if x1 < x2:
            x1,x2 = x2,x1
        total += x1//x2
        print("this is total",total)
        x1 = x1%x2
        if x1 < x2:
            x1,x2 = x2,x1
        if x2 == 0:
            print("here")
            result = x1*total
            break
    return x1,x2,result
print(gcd(7,13))
print(little(24,36))

