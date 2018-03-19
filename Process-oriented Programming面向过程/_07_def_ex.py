#-*-coding:utf-8-*-
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0的两个解。
提示：计算平方根可以调用math.sqrt()函数：
'''
import math
def ansp(a,b,delta):
    x = (-b + math.sqrt(delta)) / (2*a)
    return x

def ansm(a,b,delta):
    x = (-b - math.sqrt(delta)) / (2*a)
    return x


def quadratic(a,b,c):
    if not (isinstance(a,(int,float))and isinstance(b,(int,float)) and isinstance(c,(int,float) )):
        raise TypeError('Error Type!!!')
    delta = (b*b-4*a*c)
    if  delta < 0:
        print('delta')
        return 0
    elif delta == 0:
        x = ansp(a,b,delta)
        return x;
    else:
        x1 = ansp(a,b,delta)
        x2 = ansm(a,b,delta)
        return x1,x2

x = quadratic(2,3,1)
if x == 0:
    print("无解")
else:
    print(x)
