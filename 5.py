import sympy
#求导使用diff方法
x=sympy.Symbol('x')
f1=2*x**4+3*x+6
#参数是函数与变量
f1_=sympy.diff(f1,x)
print(f1_)
 
f2=sympy.sin(x)
f2_=sympy.diff(f2,x)
print(f2_)
 
#求偏导
y=sympy.Symbol('y')
f3=x*y+x/y
#对x，y分别求导，即偏导
f3_x=sympy.diff(f3,x)
f3_y=sympy.diff(f3,y)
f3_xx=sympy.diff(f3_x,x)
f3_yy=sympy.diff(f3_y,y)
print(f3_x)
print(f3_y)
