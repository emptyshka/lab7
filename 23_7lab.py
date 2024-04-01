import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


data = pd.read_csv('data1.csv', sep=';')
y = data.iloc[:, 0].astype('float')
x1 = data.iloc[:, 3].astype('int')
x2 = data.iloc[:, 9].astype('float')

fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].plot(x1, y)
axs[0].plot(x2, y)
fig.set_figwidth(15)
fig.set_figheight(6)
axs[0].legend(['Положение дроссельной заслонки (%)', 'Угол опережения зажигания (°ПКВ)'], loc='upper right')
axs[1].xcorr(x1, x2)
axs[1].legend(['Корреляция 4 и 10 столбцов'])
axs[0].set_title('Графики зависимости')
axs[1].set_title('График корреляции')
axs[0].set_xlabel('t, s')
axs[1].set_xlabel('%')
axs[1].set_ylabel('°ПКВ')
plt.show()

x = np.linspace(-10, 10, 100)
y = np.linspace(-0.5, 0.5, 100)
z = np.tan(x + y)
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, marker='.', color='blue')
plt.show()