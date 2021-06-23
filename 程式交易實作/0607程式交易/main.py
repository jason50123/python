x = [ i.strip('\n').split(',') for i in open('TXFA9.I020') ]

#取所有交易日
D = sorted(set( i[0] for i in x ))
#取某一日資料
y = [ i for i in x if i[0]=='20181220']
#取8:45-9:00的資料
y1 = [ i for i in y if int(i[1])>=int('084500000000') and int(i[1])<=int('090000000000')]

price = [ int(i[3]) for i in y1]
M=max(price)
m=min(price)



y2 = [ i for i in y if int(i[1])>=int('090000000000')]
date = []
for dates in D:
    date.append(dates)

for Dates in D:
    counter = 0
    if counter < 3:
        for i in y2:
            D=i[0]
            if Dates == y:
                print("True")
                T=i[1]
                P=int(i[3])
                if P>=M :
                    counter+=1
                    print(D,T,P)
                    break
                if P<=M:
                    counter+=1
                    print(D,T,P)
                    break