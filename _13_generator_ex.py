#-*-coding:utf-8-*-
'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
'''
def triangles(max):
    x = 0
    L = [1]
    while x < max:
        yield L
        L = [1]+[L[n] + L[n+1] for n in range(len(L)-1)]+[1]
        x += 1

# for u in triangles(5):
#     print(u)

for u in triangles(1):
    print(u)
