#-*-coding:utf-8-*-
#help()提供帮助方法
print(help(abs))

#abs()求绝对值，只能放入数字，arguments只能放入一个
print(abs(100))
print(abs(-110))
print(abs(12.45))
print(abs(-02.22))#输出2.22

#max()求最大值
print(max(1,2,3,4,5,6,7,8,9))
print(max(-1,-2,-9))

#类型转换
#int()
print(int('123'))
print(int(12.43))
print(float('12.34'))
print(str(456))
print(bool(1))
print(bool('x'))
print(bool(0))
print(bool(''))#false


#重点：函数名其实就是一个指向函数对象的引用，完全可以用一个别名代替、
#这点在C++语言上的处理是一个相对来说的难点，但是在Python中来说这就是一个非常容易解决的问题了
a = abs
print(a(-1))


#hex()整数类型转换为十六进制
n1 = 255
n2 = 1000
print(hex(n1),'\n',hex(n2))


#另外一种简写方式
print('n1=%s,n2=%s'%( str(hex(255)),str(hex(1000))))
