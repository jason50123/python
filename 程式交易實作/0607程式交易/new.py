x = [i.strip('\n').split(',') for i in open('TXFA9.I020')]
D = sorted(set([i[0] for i in x]))

＃n1, n2 我想設定為突破加減的比例


def Strategy1(D, n1, n2, SL):
    y = [i for i in x if i[0] == D]
    StopLoss = SL
    StopLossPrice = 0
    y1 = [i for i in y if int(i[1]) >= int(
        '084500000000') and int(i[1]) <= int('090000000000')]

    Price = [int(i[3]) for i in y1]
    M = max(Price)
    m = min(Price)
    spread = M-m

    y2 = [i for i in y if int(i[1]) >= int('090000000000')]
    BuyPrice = 0
    SellPrice = 0
    for i in y2:
        if int(i[3]) >= M+n1*spread:
            BuyPrice = int(i[3])
            BuyTime = i[1]
            StopLossPrice = BuyPrice-StopLoss
            BS = 'B'
            print("Buy Time:", BuyTime, "Buy Price:", BuyPrice)
            break
        if int(i[3]) <= m-n2*spread:
            SellPrice = int(i[3])
            SellTime = i[1]
            StopLossPrice = SellPrice+StopLoss
            BS = 'S'
            print("Sell Time:", SellTime, "Sell Price:", SellPrice)
            break

    if BuyPrice == 0 and SellPrice == 0:
        print('No trade!')

    CoveryPrice = 0
    if BS == 'B':
        y3 = [i for i in y if int(i[1]) >= int(BuyTime)]
        for i in y3:
            if int(i[3]) <= StopLossPrice:
                CoveryPrice = int(i[3])
                CoveryTime = i[1]
                print("Covery Time:", CoveryTime, "Covery Price:", CoveryPrice)
                Profit = CoveryPrice-BuyPrice
                print("Profit: ", Profit)
                break
        if CoveryPrice == 0:
            CoveryPrice = int(y3[-1][3])
            CoveryTime = y3[-1][1]
            print("Covery Time:", CoveryTime, "Covery Price:", CoveryPrice)
            Profit = CoveryPrice-BuyPrice
            print("Profit: ", Profit)
    if BS == 'S':
        y3 = [i for i in y if int(i[1]) >= int(SellTime)]
        for i in y3:
            if int(i[3]) >= StopLossPrice:
                CoveryPrice = int(i[3])
                CoveryTime = i[1]
                print("Covery Time:", CoveryTime, "Covery Price:", CoveryPrice)
                Profit = SellPrice-CoveryPrice
                print("Profit: ", Profit)
                break
        if CoveryPrice == 0:
            CoveryPrice = int(y3[-1][3])
            CoveryTime = y3[-1][1]
            print("Covery Time:", CoveryTime, "Covery Price:", CoveryPrice)
            Profit = SellPrice-CoveryPrice
            print("Profit: ", Profit)
    return(Profit)
