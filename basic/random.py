import random
import statistics
def randomData():
    data = [0,30,3,2,5]
    random.shuffle(data)
    print(data)
    data = random.random()
    data = random.choice([1,32,42,52,1])#隨機挑一個
    print("choice = ",data)
    data = random.sample([1,123,41,43,23],4)#挑4個數出來
    print(data)
    random.uniform(50,80)#產生50-80的亂數
    normalative =random.normalvariate(100,10)#取得平均數為100標準差為10的常態分配亂數
    print("normalatice = ",normalative)
def statistic_test():
    statistics.mean([1,4,7,23])#計算平均數
    statistics.median([1,43,532,123,4])#計算中位數
    statistics.stdev([12,54,23,53])#計算標準差
if __name__ == "__main__":
    randomData()