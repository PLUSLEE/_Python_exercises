#-*-coding:utf-8-*-
'''
listComprehensions是Python内置的创建list的生成式
'''

#生成[1,2,3,4,5,6,7,8,9,10]
print(list(range(1,11)))

#---------------------------

#生成1*1--9*9
L = []
for x in range(1,11):
    L.append(x * x)

print(L)

#以上步骤简化书写
print([x*x for x in range(1,11)])

#for循环加上if判断
print([x*x for x in range(1,11) if x%2==0])

#双重for循环
print([m+n for m in'ABC' for n in 'XYZ'])

#-------------------------------
#运用列表生成式可以简化代码
import os
print([d for d in os.listdir('.')])


r= {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in r.items():
     print(k,'=',v)

#列表生成式简化
print([k+'='+v for k,v in r.items()])

#list中所有的字符小写
Letter = ['Hello','Chen','Fangfang']
print([s.lower() for s in Letter])
