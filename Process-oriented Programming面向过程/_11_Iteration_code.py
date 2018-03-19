#-*-coding:utf-8-*-
'''
Python的for循环抽象程度要高于C的for循环，
因为Python的for循环不仅可以用在list或tuple上，
还可以作用在其他可迭代对象上。

python的迭代是通过for...in实现的
dict也可以迭代
dict的存储不是按照list的方式排列，迭代出的结果顺序可能不一样
dict迭代的是key，如果想要迭代value，使用for values in d.values()
'''

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for values in d.values():
    print(values)

#-----------------------------
for ch in 'ABC':
    print(ch)

#for循环，只要作用于一个可迭代的对象，for循环就可以正常进行
#判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))   #True
print(isinstance([1,2,3],Iterable)) #True
print(isinstance(123,Iterable))     #False
#整数不可迭代

#-----------------------------
#对list获取下标,enumerate（列举的意思），同时引用两个变量
for i,values in enumerate(['A','B','C']):
    print(i,values)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
