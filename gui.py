import numpy as np
import numpy.linalg as nla
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import hydraulicheadsimulate as hs
main = Tk()
main.title('机票信息查询')
#设置窗口大小
main.geometry('1000x750')
main.maxsize(1920,1080)
main.minsize(480,216)
label1 = Label(main,text='输入出发地:',font=('黑体',12))
label1.place(x = 10,y = 20,width=250,height=20)
entry1 = Entry(main,background='light sky blue')
entry1.place(x=250,y=20,width=80,height=20)

label2=Label(main,text='输入目的地:',font=('黑体',12))
label2.place(x=10,y=45,width=250,height=20)
entry2 = Entry(main,background='light sky blue')
entry2.place(x=250,y=45,width=80,height=20)

label3=Label(main,text='输入出发日期：年-月-日 如2021-09-01')
label3.place(x=10,y=70,width=250,height=20)
entry3=Entry(main,background='light sky blue')
entry3.place(x=250,y=70,width=80,height=20)
main.mainloop()