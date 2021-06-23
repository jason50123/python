import yfinance as yf
import pandas as pd
import mplfinance as fplt


def stock(stock_id):
    
    stock_id = str( stock_id ) + ".TW" # Yahoo Finance 的 代號為台灣的代號 + .TW
    data = yf.Ticker( stock_id ) # 抓取資料

    # 1mo = 1個月，max 可以把所有期間的資料都下載
    ohlc = data.history( period="36mo" )
    print(ohlc)
    data = pd.DataFrame(ohlc)
    

    data.to_csv("./"+ '/stock.csv',header = True)
    ohlc = ohlc.loc[ :, ["Open", "High", "Low", "Close", "Volume"] ] # 選擇製圖需要欄位(開高低收量)
    
    # 調整圖表標示顏色
    mc = fplt.make_marketcolors(
                                up = 'tab:red',down = 'tab:green', # 上漲為紅，下跌為綠
                                wick = {'up':'red','down':'green'}, # 影線上漲為紅，下跌為綠
                                volume = 'tab:green', # 交易量顏色
                               )
    
    s = fplt.make_mpf_style( marketcolors = mc ) # 定義圖表風格
    
    fplt.plot(
                ohlc, # 開高低收量的資料
                type = 'candle', # 類型為蠟燭圖，也就是 K 線圖
                style = s, # 套用圖表風格
                title = stock_id, # 設定圖表標題
                ylabel = 'Price ($)', # 設定 Y 軸標題
                volume = True,
                savefig='bar_chart.png', # 儲存檔案
            )