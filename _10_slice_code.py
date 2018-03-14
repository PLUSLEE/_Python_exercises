#-*-coding:utf-8-*-
'''
slice切片，用于解决制动索引范围的操作
'''

L = ['A','B','C','D']

print(L[:2])    #['A', 'B'],从正向第一个开始，不包含最后一个
print(L[1:2])   #['B']，从指定位置开始，不包含最后一个
print(L[-2:])   #['C', 'D'],从最后一个位置开始，逆向，，包含-2



L1 = list(range(100))
print(L1)

print(L1[:10:2])    #[0, 2, 4, 6, 8],前十个数，每2个取一个
print(L1[::5])      #[0, 5, 10, 15, 20, 25, 30, 35, ,从头开始到最后结束，每5个取1个
print(L1[:])    #相当于复制一个list


#tuple也可以有切片操作，只是操作结果任然是tuple
tup = (0,1,2,3,4,5,6)
print(tup[:3])  #(0, 1, 2)

#string,也相当与list，每一个字符就相当于一个数据
str = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
print(str[::2]) #ACEGIKMPRTVXZ
