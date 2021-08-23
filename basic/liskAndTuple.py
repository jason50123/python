#list 可變動列表
grades = [12,39,321,34,54]
for points in grades:
    print(points)
grades +=[123,43]
print(grades)
print(len(grades))
#tuple 不可變動列表
data = (3,4,5)
data[0] = 12#tuple's data can't be changed
print(data)