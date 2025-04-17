'''
pip install TA-lib backtesting
'''

from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import talib

from backtesting.lib import crossover

# The data imported from GOOG is a pandas dataframe containing Open/Close values, High/Low values for each day


class RsiOscillator(Strategy):
	
	upper_bound = 70
	lower_bound = 30

	def init(self):
		# RSI Window
		self.rsi_window = 14
		# self.rsi will contain the rsi parameter for every candle (day); so it will be a curve
		# the .I() method is inherited from the Strategy class
		# The self.data instead (always inherited from Strategy) contains all the data from the tick symbol GOOG we've imported in line 6. So self.data.Close contain the close price of the GOOG stock for every candle (day)
		# By passing the function we need to use to compute the indicator (talib.RSI), and the parameter needed to compute that function; RSI takes as parameter the closing price and the rsi window
		self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

	# This go through each candle, and evaluates whether it woants to buy on the next candle
	def next(self):
		# If the RSI index surpass (crossover) the self.upper_bound, that is self.rsi>self.upper_bound, we close the position (sell)
		if crossover(self.rsi, self.upper_bound):
			self.position.close()
		# If instead self.rsi<self.lower bound, the lower bound has been crossover and we buy
		elif crossover(self.lower_bound, self.rsi):
			self.position.buy()


bt = Backtest(GOOG, RsiOscillator, cash = 10_000)
stats = bt.run()
print(stats)
bt.plot()



# THIS OPTIMIZE THE PARAMETERSO OF THE STRATEGY IN ORDER TO MAXIIZE SHARP RATIO. PROBLEM: OVERFIT. IT ADJUST THE PARAMETERS IN ORDER TO GET THE BEST PERFORMANCE ON THOSE DATA.. BUT IT'S NOT SAID IT WILL ACT QUITE WELL ON NEW UNSEEN DATA
# IN ORDER TO HAVE A GOOD STRATEGY IT MUST RETURNS GOOD AMOUNTS ON DIFFERENT STOCKS (SO TRY 100 STOCKS, TEST STRATEGIES ON DIFFERENT TICKER SYMBOLS)
bt_optimize = Backtest(GOOG, RsiOscillator, cash = 10_000)
stats = bt.optimize(
		upper_bound = range(50, 85, 5),
		lower_bound = range(10,45,5),
		rsi_window = range(10,30,2),
		maximize = 'Sharpe Ratio')
print(stats)
bt.plot()