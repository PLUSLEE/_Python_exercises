#-*-coding:utf-8-*-
'''
Python的函数定义，简单但是灵活度很大。除了正常的必选参数，还可以有默认参数，可变参数和关键字参数
Preference：Java的多态
'''

def power(x):
    return x*x

def powerup(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#设置默认参数
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(powerup(2,5))
print(power(2))

'''
注意事项：
1-必选参数在前，默认参数在后，
2-如何设置默认参数
    多个参数时，变化大的参数放前面，变化小的参数放后面，变化小的参数当做默认参数
    多个参数时，可以不按顺序提供默认值，需要把参数名写上
'''

#注意默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())    #重复添加
#默认参数必须指向不变对象
'''
Python函数在定义的时候，
默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，
则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''

#优化,手动将List的内容清空
def add_end_up(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_up())
print(add_end_up())



#---------------------------------------
#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3,4])) #调用的时候需要组装一个list或者tuple
print(calc((1,2,5,7)))


def calc_up(*numbers): #定义可变参数的方法，添加*
    sum  = 0
    for n in numbers:
        sum  = sum + n * n
    return sum

print(calc_up(1,2,3,4))

#若已经有一个list或tuple
nums = [1,2,3]
print(calc_up(nums[0],nums[1],nums[2]))

#或者使用对应的*
#原理：函数内部自动组装一个tuple
print(calc_up(*nums))


#-----------------------------------------
#关键字参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'others:',kw)

#函数调用者仍然可以传入不受限制的关键字参数
print(person('Jack',24,city='Xiamen',addr='huli'))

#如果想要限制关键字参数，就可以用命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

#关键字参数必须传入参数名
print(person('Jack', 24, city='Beijing', job='Engineer'))


#-----------------------------------------
#必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

'''
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
'''
