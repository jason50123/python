# -*- coding: utf-8 -*-
import mplfinance as fplt
import yfinance as yf
import pandas as pd
def import_csv(amount):
    df = pd.read_csv("0050.csv")
    df = df.head(amount)
    df.rename(
            columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)
    # 转换为日期格式
    df['Date'] = pd.to_datetime(df['Date'])
    # 将日期列作为行索引
    df.set_index(['Date'], inplace=True)
    print(df)
    return df


def get_data_old(stock_id, period):
    stock_id = str(stock_id) + ".TW" # Yahoo Finance 的 代號為台灣的代號 + .TW
    data = yf.Ticker(stock_id) # 抓取資料
    print(data)
    # 1mo = 1個月，max 可以把所有期間的資料都下載
    ohlc = data.history(period= period)
    ohlc = ohlc.loc[:, ["Open", "High", "Low", "Close", "Volume"]] # 選擇製圖需要欄位
    return ohlc

def draw_candle_chart(df):
    
    mc = fplt.make_marketcolors(
                                up='tab:red',down='tab:green',
                                wick={'up':'red','down':'green'},
                                volume='tab:green',
                               )
    
    s  = fplt.make_mpf_style(marketcolors=mc)
    
    fplt.plot(
                df,
                type = 'candle',
                style = s,
                ylabel = 'Price ($)', 
                volume = True,
                savefig='stock_Kbar.png',
                
            )

    #plt.savefig("")
    
if __name__ == "__main__":
    
    new_df = import_csv()
    draw_candle_chart(new_df)


    
