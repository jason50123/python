# -*- coding: utf-8 -*-
import mplfinance as fplt
import yfinance as yf

def get_data(stock_id, period):
    stock_id = str(stock_id) + ".TW" # Yahoo Finance 的 代號為台灣的代號 + .TW
    data = yf.Ticker(stock_id) # 抓取資料
    
    # 1mo = 1個月，max 可以把所有期間的資料都下載
    ohlc = data.history(period= period)
    ohlc = ohlc.loc[:, ["Open", "High", "Low", "Close", "Volume"]] # 選擇製圖需要欄位
    return ohlc
    
def draw_candle_chart(stock_id, ohlc):
    
    mc = fplt.make_marketcolors(
                                up='tab:red',down='tab:green',
                                wick={'up':'red','down':'green'},
                                volume='tab:green',
                               )
    
    s  = fplt.make_mpf_style(marketcolors=mc)
    
    fplt.plot(
                ohlc,
                type = 'candle',
                style = s,
                title = stock_id,
                ylabel = 'Price ($)', 
                volume = True,
                savefig='stock_Kbar.png',
                
            )

    #plt.savefig("")
    
if __name__ == "__main__":
    draw_candle_chart(2330)
    
