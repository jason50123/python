x=[ i.strip('\n').split(',') for i in open('TXFA9.I020') ]
y=[ i for i in x if i[0]=='20181221'  and int(i[1])>=int('090000000000') and int(i[1])<=int('100000000000') ]
BuyTime=y[0][1]
BuyPrice=int(y[0][3])
SellPrice=0
StopLoss=30
StopLossPrice=BuyPrice-StopLoss
for k in y:
    if int(k[3]) <=StopLossPrice:
        SellPrice=int(k[3])
        SellTime=k[1]
    break
if SellPrice==0:
    SellTime=y[-1][1]
    SellPrice=int(y[-1][3])
print('Buy time: ',BuyTime,'Buy Price: ',BuyPrice,'Sell time: ',SellTime,'Sell Price: ',SellPrice,'\n')
Profit=SellPrice-BuyPrice
print('Profit: ',Profit,'\n')



