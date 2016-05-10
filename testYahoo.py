from yahoo_finance import Share
from pprint import pprint

yahoo = Share('SPY')
print yahoo.get_open()
print yahoo.get_price()
print yahoo.get_trade_datetime()
yahoo.refresh()

spyprice = yahoo.get_historical('2000-01-01', '2016-04-25')
pprint(yahoo.get_historical('2014-04-25', '2014-04-29'))
