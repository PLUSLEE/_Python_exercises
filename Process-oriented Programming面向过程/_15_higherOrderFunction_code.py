#-*-coding:utf-8-*-

f = abs
print(f)    #<built-in function abs>
print(f(-10))


'''
变量指向一个函数
同时这个变量，也就拥有了同样的函数功能
'''


#---------------------------------------------
#函数名也是变量
def func(x,y,f):
    return (f(x) + f(y))

print(func(-1,-1,abs))
'''
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数
以上就是高阶函数，
'''



#-------------------------------------------
'''
reduce的使用:
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

#实现序列求和
from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5,6,7,8,9]))

#求和当然可以使用sum()函数
print(sum([1,2,3,4,5,6,7,8,9]))

#reduce的功能必然比sum的使用范围更加广泛，因为可以自定义函数
#以下方法实现，连接若干数字，形成一个数
def fn(x,y):
    return x*10+y

print(reduce(fn,(1,2,3,4,5,6,7,8,9)))

#char2num
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'123456'))) #map返回的就是一个序列[]，传进来是string,


#整合以上两个函数
DIGHTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGHTS[s]
    return reduce(fn,map(char2num,s))

print(str2int('1234'))
