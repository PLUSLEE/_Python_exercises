#-*-coding:utf-8-*-
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    name = name[:1].upper()+name.lower()[1:]    #1-slice的正确使用；2-upper() and lower() 函数的正确使用
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))    #map每次执行两个参数，第一个参数时函数，第二个参数时变量
print(L2)


'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
from functools import reduce
def prod(L):
    def ride(m,n):
        return m*n
    return reduce(ride,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('1')
else:
    print('0')


'''
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456
'''
def str2float(s):
    DIGHTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    dot = s.index('.')

    def str2num(str):
        return DIGHTS[str]

    def fn(x,y):
        return x*10+y
    return reduce(fn,map(str2num,str[:dot]+str[dot+1:]))/10**dot

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('1')
else:
    print('0')
