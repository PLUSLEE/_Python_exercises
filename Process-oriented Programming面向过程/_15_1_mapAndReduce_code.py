#-*-coding:utf-8-*-

'''
map：
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回。
'''
def f(x):
    return x * x

r = map(f,(1,2,3,4,5,6,7,8,9))
print(r)    #<map object at 0x00000207646CF5F8>
print(list(r))  #[1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
由于结果r是一个Iterator，
Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''

#map()就是传说中的高阶函数
print(list(map(str,(1,2,3,4,5,6,7,8,9,0))))


#------------------------------------------------------------
