ProfitList1=[37, -35, 3, 35, 0, -8, -13, -149, 64, 0, 5, -45, 92, 16, 24, -15, 37, 10]
ProfitList2=[37, -35, 3, 35, 0, -8, -13, -19, 5, -109, 64, -45, 92, 16, 24, -15, 37, 10]

# ProfitList1總損益
TotalProfit = sum([i for i in ProfitList1])
# 總交易次數
TotalNum = len(ProfitList1)
# 平均損益
AvgProfit = round(TotalProfit/TotalNum,2)
# 總勝率
WinNum =len([i for i in ProfitList1 if i > 0])
WinRate = round(WinNum/TotalNum,2)

# 最大連續虧損 MaxContiLoss
MaxContiLoss = 0
# 當前的連續虧損
dropdown = 0
for profit in ProfitList1:
    # 計算連續虧損
    if profit <= 0:
        dropdown += profit
        # 判斷 當前連續虧損 是否為 最大連續虧損
        if dropdown < MaxContiLoss:
            MaxContiLoss = dropdown
    # 重置
    else:
        dropdown = 0

# 印出績效
print('TotalProfit:',TotalProfit)
print('TotalNum:',TotalNum)
print('AvgProfit:',AvgProfit)
print('WinRate:',WinRate)
print('MaxContiLoss:',MaxContiLoss)



###############
# ProfitList2總損益
TotalProfit = sum([i for i in ProfitList2])
# 總交易次數
TotalNum = len(ProfitList2)
# 平均損益
AvgProfit = round(TotalProfit/TotalNum,2)
# 總勝率
WinNum =len([i for i in ProfitList2 if i > 0])
WinRate = round(WinNum/TotalNum,2)

# 最大連續虧損 MaxContiLoss
MaxContiLoss = 0
# 當前的連續虧損
dropdown = 0
for profit in ProfitList2:
    # 計算連續虧損
    if profit <= 0:
        dropdown += profit
        # 判斷 當前連續虧損 是否為 最大連續虧損
        if dropdown < MaxContiLoss:
            MaxContiLoss = dropdown
    # 重置
    else:
        dropdown = 0

# 印出績效
print('TotalProfit:',TotalProfit)
print('TotalNum:',TotalNum)
print('AvgProfit:',AvgProfit)
print('WinRate:',WinRate)
print('MaxContiLoss:',MaxContiLoss)