import numpy as np

def grid(m,n):
    #将空间离散步数为m，时间离散步数为n，还需要定义L，R，t
    h = (R-L)/m
    tau = t/n
    X = np.linspace(L,R,m+1)
    T = np.linspace(0,t,n+1)
    return h,tau,X,T
def init_solution(x):
    u0 = np.zeros(x.shape)
    return u0
def ture_solution(x,t):
    return np.sin(2*np.pi*x)*t

def f(x,t):
    return  0
#np.sin(2*np.pi*x)+4*np.sin(2*np.pi*x)*t*np.pi**2

def right_solution(t):
    u = np.zeros(t.shape)
    return u

def left_solution(t):
    u = np.zeros(t.shape)
    return u


m = 100
n = 100
L = 0
R = 1
t = 1
h,tau,X,T=grid(m,n)
r = tau/h/h

U = np.zeros((len(T),len(X)))
#U[0,:] = init_solution(X)  #此处因为初值为0 ，所以不需要额外定义，如果初值为其他非0的时候就需要定义
U[:,0] = left_solution(T)
U[:,-1] = right_solution(T)


#crank_nicholson
d1 = 1 + np.ones((len(X) -2 ,))*r
d2 = 1 - np.ones((len(X) -2 ,)) *r
c = 0.5* np.ones((len(X) -3 ,)) *r
A1 = np.diag (-c , -1) + np.diag ( -c ,1) + np.diag ( d1 )
A0 = np.diag (c , -1) + np.diag (c ,1) +  np.diag( d2 )
for i in range(len(T)-1):
    F=np.zeros((len(X)-2,))
    for j in range(len(X)-2):
        F[j] = f((j+1)*h,i*tau)
    RHS = tau*F
    b = A0@U[i,1:-1].T + RHS
    U[i+1,1:-1] =np.linalg.solve(A1,b)  
#print(U)
#把真解表示出来
X,Y = np.meshgrid(X,T)
ture_U = ture_solution(X,Y)
#print(ture_U )

## 表面图
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']#可以plt绘图过程中中文无法显示的问题

fig =plt.figure(figsize=(15,7))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface( X,Y, U, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1)
plt.title("数值解")

#ax = fig.add_subplot(1, 2, 2, projection='3d')
#ax.plot_surface( X,Y,ture_U, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#ax.set_zlim(-1, 1)
#plt.title("真解")
plt.show()
