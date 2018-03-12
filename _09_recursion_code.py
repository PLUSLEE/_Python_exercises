#-*-coding:utf-8-*-

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))


'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''

#注意防止栈溢出
#RecursionError: maximum recursion depth exceeded in comparison
# print(fact(999))

#解决溢出的方法：使用尾递归
'''
所谓尾递归：在函数返回的时候，调用自身本身，
并且return本身不包含表达式
编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''
def fact_up(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num *product)

print(fact_up(1000))#然而大多数编程语言没有对尾递归进行优化，依旧会导致栈溢出
