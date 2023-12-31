#Hi im Dogukan

import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display
# import pytz module for working with time zone
import pytz

account_number = xxx  # Hesap No
pass1 = 'pass1'  # Şifre
server1 = 'FTMO-Demo' # Server
mt5.initialize(login=account_number, password=pass1, server=server1)

if not mt5.initialize():
    print("MetaTrader 5 sunucusuna bağlanılamadı")
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2017, 6, 13, tzinfo=timezone)
utc_to = datetime(2019, 6, 15, hour=12, tzinfo=timezone)
# get data
rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_M15, utc_from, utc_to)

mt5.shutdown()


#print("Display obtained data 'as is'")
#for rate in rates:
#    print(rate)



# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

candlestick = go.Candlestick(
    x=rates_frame['time'],
    open=rates['open'],
    high=rates['high'],
    low=rates['low'],
    close=rates['close']
)

fig = go.Figure(data=[candlestick])
fig.show()

#display data
print("\nDisplay dataframe with data")
print(rates_frame)
