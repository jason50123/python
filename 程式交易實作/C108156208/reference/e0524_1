ProfitList=[37, -35, 3, 35, 0, -8, -13, -149, 64, 0, 5, -45, 92, 16, 24, -15, 37, 10]
import matplotlib.pyplot as plt
#定義圖表物件
plt.figure(figsize=(12,8))
ax = plt.subplot(111)
#繪製圖案 ( X軸物件, Y軸物件, 線風格 )
ax.plot(ProfitList, 'k-' , linewidth=1 )
#定義標頭
ax.set_title('Profit List')
plt.show()

# 績效列表
ProfitList=[37, -35, 3, 35, 0, -8, -13, -149, 64, 0, 5, -45, 92, 16, 24, -15, 37, 10]
# 累計績效列表
# AProfitList=[37,37-35,37-35+3, 37-35+3+35, 37-35+3+35+0,.....]
AProfitList=[]
S=0
for i in ProfitList:
 S=S+i
 AProfitList.append(S)

plt.figure(figsize=(12,8))
ax = plt.subplot(111)
ax.plot(AProfitList, 'k-' , linewidth=1 )
ax.set_title('Sum of Profit List')
plt.show()

績效圖與累計績效圖畫在一起
plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(ProfitList, 'k-' , linewidth=1 )
ax2.plot(AProfitList, 'k-' , linewidth=1 )
ax.set_title('Sum of Profit List')
plt.show()

比較兩個績效列表
ProfitList1=[37, -35, 3, 35, 0, -8, -13, -149, 64, 0, 5, -45, 92, 16, 24, -15, 37, 10]
ProfitList2=[37, -35, 3, 35, 0, -8, -13, -19, 5, -109, 64, -45, 92, 16, 24, -15, 37, 10]

AProfitList1=[]
S=0
for i in ProfitList1:
 S=S+i
 AProfitList1.append(S)


AProfitList2=[]
S=0
for i in ProfitList2:
 S=S+i
 AProfitList2.append(S)

plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax1.set_ylim([-150,100])
ax1.plot(AProfitList1, 'k-' , linewidth=1 )
ax2 = plt.subplot(212)
ax2.set_ylim([-150,100])
ax2.plot(AProfitList2, 'r-' , linewidth=1 )
#定義標頭
ax.set_title('Sum of Profit List')
plt.show()

比較兩個績效列表
ProfitList1=[37, -35, 3, 35, 0, -8, -13, -149, 64, 0, 5, -45, 92, 16, 24, -15, 37, 10]
ProfitList2=[37, -35, 3, 35, 0, -8, -13, -19, 5, -109, 64, -45, 92, 16, 24, -15, 37, 10]

AProfitList1=[]
S=0
for i in ProfitList1:
 S=S+i
 AProfitList1.append(S)


AProfitList2=[]
S=0
for i in ProfitList2:
 S=S+i
 AProfitList2.append(S)

plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax1.set_ylim([-150,100])
ax1.plot(AProfitList1, 'k-' , linewidth=1 )
ax2 = plt.subplot(212)
ax2.set_ylim([-150,100])
ax2.plot(AProfitList2, 'r-' , linewidth=1 )
#定義標頭
ax.set_title('Sum of Profit List')
plt.show()

# Python操作
KBar = {}
import numpy as np
x=[10.,11.,12.,15.,10.,8.,15.,18.,19.,15.,14.]
KBar['P'] = np.array(x)
y=talib.SMA(KBar['P'],5)

# 繪圖參考
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
ax = plt.subplot(111)
ax.plot( x, 'k-' , linewidth=1 )
ax.plot( y, 'r-' , linewidth=1 )
plt.show()