'''2D-steady_state-flow-confined-aquifer-hydraulic-head-simulate.py'''
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
                #上下左右边界赋值3
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

def main_():
    s=float(entry1.get())
    x=int(entry2.get())
    y=int(entry3.get())
    ht=int(entry4.get())
    hb=int(entry5.get())
    hl=int(entry6.get())
    hr=int(entry7.get())
    if va.get()=='1':
        L_R_NOFLOW=True
    else:
        L_R_NOFLOW=False 
    H_all=hydraulic_head_finite_difference_calaculate(step_length=s,X_length=x,Y_length=y,H_top=ht,H_bottom=hb,H_left=hl,H_right=hr,L_R_NOFLOW=L_R_NOFLOW)
    draw_3D_hydraulic_head(step_length=s,X_length=x,Y_length=y,H_ALL=H_all)

'''if __name__=="__main__":
    main()
    print('hello world')'''

main = Tk()
main.title('承压含水层稳定二维流有限差分模拟')
#设置窗口大小
main.geometry('400x350')
main.maxsize(1920,1080)
main.minsize(280,200)
label1 = Label(main,text='输入差分步长:',font=('黑体',12))
label1.place(x = 10,y = 20,width=250,height=20)
entry1 = Entry(main,background='light sky blue')
entry1.place(x=250,y=20,width=80,height=20)

label2=Label(main,text='输入限定X轴长度:',font=('黑体',12))
label2.place(x=10,y=45,width=250,height=20)
entry2 = Entry(main,background='light sky blue')
entry2.place(x=250,y=45,width=80,height=20)

label3=Label(main,text='输入限定Y轴长度:',font=('黑体',12))
label3.place(x=10,y=70,width=250,height=20)
entry3=Entry(main,background='light sky blue')
entry3.place(x=250,y=70,width=80,height=20)

label4=Label(main,text='输入上部水头:',font=('黑体',12))
label4.place(x=10,y=95,width=250,height=20)
entry4=Entry(main,background='light sky blue')
entry4.place(x=250,y=95,width=80,height=20)

label5=Label(main,text='输入下部水头:',font=('黑体',12))
label5.place(x=10,y=120,width=250,height=20)
entry5=Entry(main,background='light sky blue')
entry5.place(x=250,y=120,width=80,height=20)

label6=Label(main,text='输入左侧水头:',font=('黑体',12))
label6.place(x=10,y=145,width=250,height=20)
entry6=Entry(main,background='light sky blue')
entry6.place(x=250,y=145,width=80,height=20)

label7=Label(main,text='输入右侧水头:',font=('黑体',12))
label7.place(x=10,y=170,width=250,height=20)
entry7=Entry(main,background='light sky blue')
entry7.place(x=250,y=170,width=80,height=20)

label8=Label(main,text='是否左右无流',font=('黑体',12))
label8.place(x=10,y=195,width=250,height=20)

va=StringVar()
radiobutton1 = Radiobutton(main,text='是',variable=va,value='1',font=('黑体',12))
radiobutton1.place(x=50,y=220,width=75,height=20)
radiobutton2 = Radiobutton(main,text='否',variable=va,value='0',font=('黑体',12))
radiobutton2.place(x=150,y=220,width=75,height=20)

button1=Button(main,text='计算',background='SeaGreen2',command=main_,font=('黑体',12))
button1.place(x=135,y=250,width=40,height=20)

main.mainloop()