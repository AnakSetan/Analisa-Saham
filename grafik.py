import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
# x = [``]
ax = plt.subplot(111, projection='3d')

df = pd.read_csv('x.csv')
# print(list(df['x']))

# x = np.repeat(0, 10)
# z = x
x = np.arange(0,20,2)
y = np.repeat (0,10)
y1 = np.repeat (5,10)
z = np.repeat(0,10)
# y = np.arange(0,20,2)

dx = np.repeat(1,10)
dy = dx
dz = list(df['z'])

# plt.plot(list(df['x']), list(df['y']))
# plt.show()

ax.bar3d(x,y,z,dx,dy,dz)
# ax.bar3d(x,y1,z,dx,dy,dz)
plt.show()
# print(y)