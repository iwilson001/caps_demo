import backtrader as bt
import yfinance as yf
from IPython.core.display import display

from yahoo_fin.stock_info import get_data



class PrintClose(bt.Strategy):

    def __init__(self):
        #Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(self.datas[0].datetime.date(0).strftime('%Y/%m/%d') + ', ' + f' {txt} {dt}' )
        #print(f'{dt} {txt}') #Print date and close

    def next(self):
        self.log('Close: ', self.dataclose[0])

#Instantiate Cerebro engine
cerebro = bt.Cerebro()

#Add data feed to Cerebro
# sobr_daily = get_data("sobr", start_date="11/27/2022", end_date="12/09/2022", index_as_date = True, interval="1d")
# sobr_daily

#sobr_data = bt.feeds.PandasData(dataname=yf.download('SOBR', '2022-11-27', '2022-12-09'))
# display(sobr_data)

data = bt.feeds.YahooFinanceCSVData(dataname='SOBR.csv')
cerebro.adddata(data)

#Add strategy to Cerebro
cerebro.addstrategy(PrintClose)

#Run Cerebro Engine
cerebro.run()
