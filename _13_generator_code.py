#-*-coding:utf-8-*-
'''
列表生成式，生成的数据很完整，但是假如只需要生成的list 的前几个，就使用generator
generator生成器，一边循环一边计算
'''

#列表生成式
L = [x*x for x in range(10)]
print(L)

#生成器
G = (x*x for x in range(10))
print(G)

'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
<generator object <genexpr> at 0x00000289428D50F8>
'''

#generator是可迭代对象，所以使用for循环打印
for n in G:
    print(n)

#-----------------------------------
#斐波拉契数列使用list生成式写不出来，但是使用generator可以实现
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b=b,a+b   #(a,b)=(b,a+b)
        n+=1
    return 'done'

fib(10)

#-----------------------------------
#将斐波拉契数列的生成方式和generator的原理结合起来，两者非常相似
def fib_up(max):
    n,a,b = 0,0,1
    while n < max:
        yield b #generator在每次调用next()执行，yield语句返回；再次执行fib时，从上次yield的语句继续执行
        a,b=b,a+b   #(a,b)=(b,a+b)
        n+=1
    return 'done'

for n in fib_up(10):
    print(n)
