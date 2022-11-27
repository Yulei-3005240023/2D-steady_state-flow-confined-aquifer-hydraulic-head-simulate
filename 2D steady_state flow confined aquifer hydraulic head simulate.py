import numpy as np
import numpy.linalg as nla
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
#仅适用于椭圆方程
def hydraulic_head_finite_difference_calaculate(step_length,X_length,Y_length,H_top,H_bottom,H_left,H_right,L_R_NOFLOW=False):
    if(L_R_NOFLOW==True):
        X_length=7*X_length
    #X,Y轴单元格的数目
    m=int(X_length/step_length)
    n=int(Y_length/step_length)
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
                H_a[l,i*m+j]=-4#高斯-赛德尔迭代法??
                l+=1
    #解矩阵方程
    H=nla.solve(H_a,H_b)
    q=0
    while q<m*n:
        for i in range(0,n):#对行进行扫描
            for j in range(0,m):#对列进行扫描
                H_ALL[i,j]=H[q]
                q+=1   
    if(L_R_NOFLOW==True):
        a=int((m/7)*3)
        b=int((m/7)*4)
        H_ALL=H_ALL[:,a:b]

    return H_ALL

def draw_3D_hydraulic_head(step_length,X_length,Y_length,H_ALL):
    #X,Y轴单元格的数目
    m=int(X_length/step_length)
    n=int(Y_length/step_length)
    #X轴
    X = np.linspace(0,X_length,m)
    #Y轴 
    Y =np.linspace(0,Y_length,n)
    #定义初值
    X,Y = np.meshgrid(X,Y)
    #可以plt绘图过程中中文无法显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #解决负号为方块的问题
    plt.rcParams['axes.unicode_minus'] = False   
    fig =plt.figure(figsize=(10,7))
    ax = fig.add_subplot( projection='3d')
    ax.plot_surface( X,Y,H_ALL,linewidth=0, antialiased=True,cmap=plt.get_cmap('rainbow'))
    ax.set_zlim(0, 1)
    plt.title("差分数值解(差分步长%s)"%step_length)
    plt.show()

def main():
    s=0.5
    x=10
    y=10
    ht=1
    hb=0
    hl=0
    hr=0
    H_all=hydraulic_head_finite_difference_calaculate(step_length=s,X_length=x,Y_length=y,H_top=ht,H_bottom=hb,H_left=hl,H_right=hr,L_R_NOFLOW=False)
    draw_3D_hydraulic_head(step_length=s,X_length=x,Y_length=y,H_ALL=H_all)

if __name__=="__main__":
    main()
    print('hello world')