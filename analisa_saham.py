import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
#------------SAHAM TELKOMSEL-------------------
dfTlkm = pd.read_csv(
    'telkomsel.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfTlkm.set_index('Tanggal', inplace = True)
dfTlkm = dfTlkm.sort_index()
print(dfTlkm)
# #-----------SAHAM INDOSAT----------------------
dfIsat = pd.read_csv(
    'indosat.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfIsat.set_index('Tanggal', inplace = True)
dfIsat = dfIsat.sort_index()
# # print(dfIsat)
# #----------SAHAM XL----------------------------
dfXcl = pd.read_csv(
    'xl.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfXcl.set_index('Tanggal', inplace = True)
dfXcl = dfXcl.sort_index()
# # print(dfXcl)
# #-----------SAHAM FREN------------------------
dfFren = pd.read_csv(
    'fren.csv',
    index_col= False,
    parse_dates=['Tanggal']
)
dfFren.set_index('Tanggal', inplace = True)
dfFren = dfFren.sort_index()
# # print(dfFren)

# #---------------PLOTING GRAFIK---------------
plt.style.use('seaborn')
plt.plot(
    dfTlkm.index, dfTlkm['Close'],'r-',
    dfIsat.index, dfIsat['Close'],'g-',
    dfXcl.index, dfXcl['Close'],'b-',
    dfFren.index, dfFren['Close'],'y-',
)
#---------------Set AXIS----------------------
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(
    interval=3
))
ax.xaxis .set_major_formatter(mdates.DateFormatter(
    '%b %y'
))
plt.title('Harga Grafik Saham TLKM, EXCL, ISAT, FREN')
plt.xlabel('Time')
plt.ylabel('Rp')
plt.legend(['TLKM','ISAT','FREN','EXCL'])
plt.xticks(rotation = 45)
plt.show()