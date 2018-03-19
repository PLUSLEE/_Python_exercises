#-*-coding:utf-8-*-

'''
请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''

L = ['Bart', 'Lisa', 'Adam']

#正向输出
for x in L:
    print("Hello,"+ x +"!")

#反向输出
lengthL = len(L)
while lengthL > 0:
    print("Hello,"+L[lengthL-1])
    lengthL-=1
