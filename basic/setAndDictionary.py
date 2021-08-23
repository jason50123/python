s1 = {3, 4, 5}
s2 = {5, 6, 7}
s3 = s1 & s2 #交集
s4 = s1 | s2 #聯集
s5 = s2 - s1 #指從s2中減去在S1重複的資料
s6= s1 ^ s2 #反交集
print(s6)
#set(字串)
s7=set("hello")
print(s7)
#------------------------------------------
#字典key:value
dic = {"apple" : "蘋果", "banana" : "香蕉"}
dic["apple"] = "新蘋果"
print("apple" in dic)
print("pine apple" in dic)
del dic["apple"]
print(dic)
numberdic = {x:x*2 for x in [3,4,5]}
print(numberdic)