import numpy as np
from numpy import sin,cos,pi,exp

def grid(m,n):
    """
    #此处默认X轴和Y轴剖分步长一样
    """
    h = (R-L)/m  
    tau = t/n
    X1 = np.linspace(L,R,m+1)  #X轴
    X2 = np.linspace(U,D,m+1)  #Y轴
    T = np.linspace(0,t,n+1)
    return h,tau,X1,X2,T  #X为空间方向的节点，T为时间方向的节点

def ture_u(x,y,t):
    return exp(-t)*sin(pi*x)*sin(pi*y)

def init_u(x,y):
    return sin(pi*x)*sin(pi*y)

def right_solution(t):
    u = np.zeros(t.shape)
    return u

m = 10
n = 10
U = 0
D = 1
L = 0
R = 1
t = 1
h,tau,X1,X2,T=grid(m,n)
r = tau/h/h/(1)

U = np.zeros((len(X1),len(X2),len(T)))


#crank_nicholson
node = (len(X1))*(len(X1))   #自由度个数
d1 = np.ones((node,))*(-2*r+1)
d2 = np.ones((node,))*(2*r+1)

d3 = np.ones((node - 1,))*(r/2)
d4 = np.ones((node - len(X1),))*(r/2)

A1 = np.diag(d2) - np.diag(d3,-1) - np.diag(d3,1) - np.diag(d4,- len(X1)) - np.diag(d4, len(X1))
A0 =  np.diag(d1) + np.diag(d3,-1) + np.diag(d3,1) + np.diag(d4,- len(X1)) + np.diag(d4, len(X1))


#定义初值
X1,X2 = np.meshgrid(X1,X2)
U[:,:,0] = init_u(X1,X2)


for i in range(len(T)-1):
    U_NEW = U[:,:,i].reshape(-1)   #展开为一个一维的向量
    b = A0@U_NEW
    U_NEW = np.linalg.solve(A1,b)  
    U[:,:,i+1] = U_NEW.reshape(11,-1)   #再用reshape改变回来
    
    #强制改变边界条件
    U[:,-1,i+1] = 0
    U[:,0,i+1] = 0
    U[-1,:,i+1] = 1
    U[0,:,i+1] = 0
#print(U[:,:,-1])
TURE_U = ture_u(X1,X2,1)   #t =1 时刻真解
print(X1)


## 表面图
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']#可以plt绘图过程中中文无法显示的问题
plt.rcParams['axes.unicode_minus'] = False   #解决负号为方块的问题

fig =plt.figure(figsize=(15,7))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface( X1,X2, U[:,:,-1], cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1, 1)
plt.title("数值解")

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_surface( X1,X2,TURE_U, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1, 1)
plt.title("真解")
plt.show()

