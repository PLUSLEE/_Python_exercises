#-*-coding:utf-8-*0-
'''
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y
'''

def product(*x):
    mul = 1
    for i in x:
        if not isinstance(i,(int,float)):
            raise TypeError('TypeError')
        mul = mul * i
    return mul

print(product(1,2))
print(product(0,0,0,0,1))
print(product(1,2,3,4,5,6,7,8,9))
print(product(1,'1'))
