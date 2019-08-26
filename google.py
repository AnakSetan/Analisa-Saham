import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dfGoogle = pd.read_csv('GOOG.csv',
index_col= False,
parse_dates=['Date'])
dfGoogle.set_index('Date', inplace = True)
dfTlkm = pd.read_csv('telkomsel.csv',
index_col= False,
parse_dates=['Tanggal'])
dfTlkm.set_index('Tanggal',inplace = True)
dfTlkm = dfTlkm.sort_index()

google = dfGoogle['2018-09-01':'2019-08-01']['Close']*14000
# print(dfGoogle['Close'])
plt.plot(dfGoogle['2018-09-01':'2019-08-01'].index, google,'r-',
dfTlkm['2018-09-01':'2019-08-01'].index, dfTlkm['Close'],'b-')
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.show()