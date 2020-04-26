n = input()
x= n.split(",")
x = sorted(x)
del x[2]
print (max(x))
