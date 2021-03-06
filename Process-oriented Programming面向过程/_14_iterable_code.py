#-*-coding:utf-8-*-
#直接作用于for循环的对象统称为可迭代对象：Iterable
from collections import Iterable

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

#---------------------------------------
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections import Iterator

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x for x in range(10)),Iterator))

'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
'''
