import datetime
import backtrader as bt
from backtrader.indicators import AverageTrueRange

from strategies import *



if __name__ == '__main__':
    # Instantiate Cerebro engine
    cerebro = bt.Cerebro()

    # Set data parameters and add to Cerebro
    data = bt.feeds.YahooFinanceCSVData(
        dataname='SOBR.csv',
        # fromdate=datetime.datetime(2016, 1, 1),
        # todate=datetime.datetime(2017, 12, 25),
    )
    # settings for out-of-sample data
    # fromdate=datetime.datetime(2018, 1, 1),
    # todate=datetime.datetime(2019, 12, 25))

    cerebro.adddata(data)

    # Add strategy to Cerebro
    cerebro.addstrategy(MAcrossover)

    # Default position size
    cerebro.addsizer(bt.sizers.SizerFix, stake=3)
    # Run Cerebro Engine
    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')