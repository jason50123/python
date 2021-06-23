print('交易次數:', TotalTreadeNum, '總盈虧:', sum(TotalProfit))
result = pd.DataFrame(data)
print(result)
self.change_data(result, self.ui.tableWidget)

KPI_dict = {'交易次數': [TotalTreadeNum],
            '總盈虧': [sum(TotalProfit)]
            }
KPI_df = pd.DataFrame(KPI_dict)
self.change_data(KPI_df, self.ui.tableWidget_2)

import matplotlib.pyplot as plt  # 匯出績效圖表
import matplotlib.ticker as plticker
plot_X = list(range(1, len(TotalProfit) + 1))
plot_Y = np.cumsum(TotalProfit)
ax = plt.subplot(111)           # 新增繪圖圖片

ax.bar(plot_X, plot_Y)      # 繪製圖案 ( X軸物件, Y軸物件 )
ax.ticklabel_format(style="plain")  # 設定Y軸為實數顯示，否則預設顯示為科學符號

# 設定X軸間隔為1
# this locator puts ticks at regular intervals
loc = plticker.MultipleLocator(base=1.0)
ax.xaxis.set_major_locator(loc)

# 設定文字
for x, y in zip(plot_X, plot_Y):
    text_show = int(y)
    # plt.text(X座標, Y座標, 顯示內容, 水平對齊方式, 垂直對齊方式)
    if y > 0:
        plt.text(x, y, text_show, ha="center", va="bottom")
    else:
        plt.text(x, y, text_show, ha="center", va="top")

plt.savefig("bar_chart.png")
self.change_plot("bar_chart.png")


def result(self,pd,np):
    