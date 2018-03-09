#-*-coding:utf-8-*-
print(1+2+3)

#for...in循环，依次把list或者tuple中的每一个元素迭代出来
classmate = ["Lee",'CFF','LZ']

for name in classmate:
    print(name)

#输出1-10之和
sum = 0
for x in[1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

#rang()函数可以自动生成序列数,然后通过list()函数将序列数转化为list
#生成的数字不包含本身，包含最开的0
ls = list(range(10))
for x in ls:
    print(x)

#同样的方法，输出0-100之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)



#-------------------------------------------------------
#while循环，只要条件满足就重复循环

#计算100以内的所有奇数之和
sum = 0
n = 99
while n >0:
    sum = sum +n
    n-=2
print(sum)


#-------------------------------------------------------

#break和continue的用途
'''
break是直接中断循环
continue是跳过当前这次循环，直接执行下一次
'''

#这是一个死循环
while 1:
    print("Dead")
