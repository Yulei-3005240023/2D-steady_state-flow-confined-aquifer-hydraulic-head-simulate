import numpy as np
import numpy.linalg as nla
#预设步长为2
h=2
#预设X,Y轴边界长度均为10
a=10
b=10
#X,Y轴单元格的数目
m=int(a/h)
n=int(b/h)
#X轴
X = np.linspace(0,a,m)
#Y轴 
Y =np.linspace(0,b,n)
#定义初值
X,Y = np.meshgrid(X,Y)
#预设上下左右边界初值
H_top=1
H_bottom=0
H_left=0
H_right=0
#创建一个全部值为0的矩阵
H_ALL=np.zeros((n,m))
#常数b矩阵
H_b=np.zeros((m*n,1))
#系数a矩阵
H_a=np.zeros((m*n,m*n))
l=0
while l<m*n:
    for i in range(0,n):#对行进行扫描
        for j in range(0,m):#对列进行扫描
            #上下左右边界赋值
            if((i-1)<0):
                H_b[l]=H_b[l]-H_top
            if((j-1)<0):
                H_b[l]=H_b[l]-H_left
            if((i+1)==n):
                H_b[l]=H_b[l]-H_bottom
            if((j+1)==m):
                H_b[l]=H_b[l]-H_right
            #给位置为(i-1,j)处的水头赋上系数值
            if((i-1)>=0):
                H_a[l,(i-1)*m+j]=1
            #给位置为(i+1,j)处的水头赋上系数值
            if((i+1)<n):
                H_a[l,(i+1)*m+j]=1
            #给位置为(i,j-1)处的水头赋上系数值
            if((j-1)>=0):
                H_a[l,i*m+j-1]=1
            #给位置为(i,j+1)处的水头赋上系数值
            if((j+1)<m):
                H_a[l,i*m+j+1]=1
            #给位置为（i,j)处的水头赋上系数值
            H_a[l,i*m+j]=-4
            l+=1
#解矩阵方程
H=nla.solve(H_a,H_b)
q=0
while q<m*n:
    for i in range(0,n):#对行进行扫描
        for j in range(0,m):#对列进行扫描
            H_ALL[i,j]=H[q]
            q+=1
print(X)   
print(Y)      
            
## 表面图
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']#可以plt绘图过程中中文无法显示的问题
plt.rcParams['axes.unicode_minus'] = False   #解决负号为方块的问题

fig =plt.figure(figsize=(10,7))

ax = fig.add_subplot( projection='3d')
ax.plot_surface( X,Y,H_ALL,linewidth=0, antialiased=False,cmap=plt.get_cmap('rainbow'))
ax.set_zlim(0, 1)
plt.title("差分数值解(差分步长%s)"%h)
plt.show()