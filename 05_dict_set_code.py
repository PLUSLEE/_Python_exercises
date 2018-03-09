#-*-coding:utf-8-*-
#key-value，一一对应；如果一个key键入多个值，后面的值会顶替之前的值
d = {'Mi':95,'Bob':98,'ff':100}
print(d['Mi'])

'''
为避免key不存在
1-通过'key'in d   进行判断
2-通过d.get('key') 进行查找，空，返回None
或者d.get('key',-1)返回指定的数值
'''
print('ff'in d)
print('lz'in d)
print(d.get('lz'))
print(d.get('lz',-1))
print(d.pop('Bob'))

'''
dictionary用空间换时间
list用时间换空间
'''


#-------------------------------------
'''
set一组key集合，但是不存储value
init set,you should provided a list as input
'''
s = set([1,2,3])
print(s)

s.add(4)
s.remove(1)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合
#因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
sx1 = s1 & s2
sx2 = (s1 | s2)
print(sx1,sx2)
