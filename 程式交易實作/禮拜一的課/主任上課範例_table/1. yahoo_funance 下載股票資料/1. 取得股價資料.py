# -*- coding: utf-8 -*-
import yfinance as yf

stock_id = "2330"
stock_id = str( stock_id ) + ".TW" # Yahoo Finance 的 代號為台灣的代號 + .TW
data = yf.Ticker( stock_id ) # 抓取資料

# 1mo = 1個月，max 可以把所有期間的資料都下載
ohlc = data.history( period="2mo" )
print( ohlc )