import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('telkomsel.csv',
index_col= False,
parse_dates=['Tanggal'])
# df.set_index('Tanggal',inplace = True)#Cara pertama menentukan tanggal sebagai index
df = df.set_index('Tanggal')#cara kedua menentukan tanggal sebagai index
df = df.sort_index()
#-----------------------------------------------------
# print(df['2016-01':'2017-01'])#mencari data saham TLKM dari Januari 2016-Januari 2017
#-----------------------------------------------------
# print('------------------------------------------------')
# print('Harga Maksimal TLKM : Rp',df.loc['2019-03']['Close'].max())
# print('Harga Minimum TLKM : Rp',df.loc['2019-03']['Close'].min())
# print('------------------------------------------------')
#mencari di tanggal berapa yang memiliki harga close paling tinggi
# print(df[df['Close']== df['Close'].max()])
#-----------Membuat grafik nya---------------------------------------------
# plt.style.use ('seaborn')
# plt.plot(
#     df.index,
#     df['Close'],
#     'r-'
# )
# print(df['2019-02-01':'2019-05-01'].count())
# plt.subplots_adjust(bottom= .21)
# plt.grid (True)
# plt.xlabel('Date')
# plt.ylabel('Rp')
# plt.xticks(rotation = 45)
# #SET AXIS-------------------------------------
# ax = plt.gca()#gca = Get Current Axis (Sumbu)
# ax.xaxis.set_major_locator(mdates.MonthLocator(
#     interval=3
# ))
# ax.xaxis.set_major_formatter(mdates.DateFormatter(
#     '%d-%m-%Y'
# ))
# plt.title('GRAFIK CLOSE SAHAM TLKM')
# plt.show()
#----------------------------------------
#RESAMPLE
# print(df['Close'].resample('M').mean())# 'M' Itu MonthEnd (AkhirBUlan) Rata-rata closing setiap akhir bulan (bagus untuk report)
# print(df['2019-02':'2019-05']['Close'].resample('W').mean())# 'W' itu WeekEnd (AkhirMinggu)
print(df['2017-02':'2019-02']['Close'].resample('Q').mean())