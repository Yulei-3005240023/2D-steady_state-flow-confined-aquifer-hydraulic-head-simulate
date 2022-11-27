import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure() #定义新的三维坐标轴

ax3 = plt.axes(projection= '3d')

#定义三维数据

x = np.arange(- 10, 10, 100)

y = np.arange(- 10, 10, 100)

X, Y = np.meshgrid(x, y)

Z = np.sin(X)+np.cos(Y)

#作图

ax3.plot_surface(X,Y,Z,cmap= 'rainbow')

ax3.contour(X,Y,Z, zdim='z',offset=-2,cmap='rainbow') #等高线图，要设置offset，为Z的最小值

plt.show()