from os import close, name
import mplfinance as fplt
from pandas.core.base import DataError
import yfinance as yf
import pandas as pd
import numpy as np
import talib

def calaulate(ma_day_input,multiply):
    df = pd.read_csv("0050.csv")
    print(df)
    df["收盤價"] = df["close"] 
    df["成交量"] = df["volume"]
    df["賣出價"] = df["收盤價"].shift(-3)
    
    df = df.loc[:,["date", "收盤價", "成交量", "賣出價"]]
    print("new_df",df)
    close_ma_caculate = talib.SMA(df["收盤價"],ma_day_input)
    volume_ma_caculate = talib.SMA(df["成交量"],ma_day_input)
    condition1 = df["收盤價"] > close_ma_caculate
    condition2 = df["成交量"] > (volume_ma_caculate)*multiply
    df = df[(condition1 & condition2)]
    df["損益"] = ( df["賣出價"] - df["收盤價"] ) * 1000 
    
    print(df)
    total_profit = df["損益"].sum() 
    avg_profit = df["損益"].mean() 
    trade_times = df["損益"].count()

    output = "總收益 = ", (round(total_profit,2)) , " 平均收益 = ", (round(avg_profit,2)) , " 交易次數 = " , (trade_times)

    print (output)
    return df



if __name__ == "__main__" :
    calaulate(5,1.2)