import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#------------SAHAM APPLE Inc.
dfApple = pd.read_csv(
    'AAPL.csv',
    index_col= False,
    parse_dates=['Date']
)
dfApple.set_index('Date', inplace = True)
dfApple = dfApple.sort_index()
# print(dfApple)
apple = dfApple['2018-09-01':'2019-08-01']['Close']*14282.60
#------------SAHAM FaceBook Inc.
dfFb = pd.read_csv(
    'FB.csv',
    index_col= False,
    parse_dates=['Date']
)
dfFb.set_index('Date', inplace = True)
dfFb = dfFb.sort_index()
fb = dfFb['2018-09-01':'2019-08-01']['Close']*14282.60
# #------------SAHAM Google Inc.
dfGoogle = pd.read_csv(
    'GOOG.csv',
    index_col= False,
    parse_dates=['Date']
)
dfGoogle.set_index('Date', inplace = True)
dfGoogle = dfGoogle.sort_index()
google = dfGoogle['2018-09-01':'2019-08-01']['Close']*14282.60
# #------------SAHAM Microsoft Inc.
dfMicro = pd.read_csv(
    'MSFT.csv',
    index_col= False,
    parse_dates=['Date']
)
dfMicro.set_index('Date', inplace = True)
dfMicro = dfMicro.sort_index()
microsoft = dfMicro['2018-09-01':'2019-08-01']['Close']*14282.60
# print(dfMicro)
#---------------SAHAM TELKOMSEL----------------------
dfTlkm = pd.read_csv(
    'telkomsel.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfTlkm.set_index('Tanggal', inplace = True)
dfTlkm = dfTlkm.sort_index()
telkomsel = dfTlkm['2018-09-01':'2019-08-01']['Close']
# print(dfTlkm)
# #-----------SAHAM INDOSAT----------------------
dfIsat = pd.read_csv(
    'indosat.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfIsat.set_index('Tanggal', inplace = True)
dfIsat = dfIsat.sort_index()
indosat = dfIsat['2018-09-01':'2019-08-01']['Close']
# # print(dfIsat)
# #----------SAHAM XL----------------------------
dfXcl = pd.read_csv(
    'xl.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfXcl.set_index('Tanggal', inplace = True)
dfXcl = dfXcl.sort_index()
exel = dfXcl['2018-09-01':'2019-08-01']['Close']
# # print(dfXcl)
# #-----------SAHAM FREN------------------------
dfFren = pd.read_csv(
    'fren.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfFren.set_index('Tanggal', inplace = True)
dfFren = dfFren.sort_index()
fren = dfFren['2018-09-01':'2019-08-01']['Close']
# print(dfFren)
# #-------Ploting Grafik---------------
plt.style.use('seaborn')
plt.plot(
    dfApple['2018-09-01':'2019-08-01'].index, apple,'r-',
    dfFb['2018-09-01':'2019-08-01'].index, fb, 'b-',
    dfGoogle['2018-09-01':'2019-08-01'].index, google,'y-',
    dfMicro['2018-09-01':'2019-08-01'].index, microsoft,'g-',
    dfTlkm['2018-09-01':'2019-08-01'].index, telkomsel,'r--',
    dfIsat['2018-09-01':'2019-08-01'].index, indosat,'b--',
    dfXcl['2018-09-01':'2019-08-01'].index, exel,'y--',
    dfFren['2018-09-01':'2019-08-01'].index, fren,'g--' 
)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %y'))
plt.title('Harga Saham Apple Inc., Microsoft Inc., Google Inc., Facebook Inc., Telkomsel, Indosat, XL, SmartFren')
plt.xlabel('TIME')
plt.ylabel('Dalam Rp')
plt.legend(['Apple','Facebook','Google','MicroSoft','Telkomsel','Indosat','XL','Smartfren'])
plt.xticks(rotation = 45)
plt.show()