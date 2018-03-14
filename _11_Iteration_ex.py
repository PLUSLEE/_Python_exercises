#-*-coding:utf-8-*-
'''
请使用迭代查找一个list中最小和最大值，
并返回一个tuple：
'''

def findMinAndMax(L):
    if not isinstance(L,list):
        raise TypeError('ensue input is List')
    for i in L:
        if not  isinstance(i,int):
            raise TypeError('ensure in list ,each element is int number')

    lenL = len(L)
    if len == 0:
        return(None,None)
    max = L[0]
    min = L[0]
    for i in L:
        if max < i:
            max = i
        if min > i:
            min = i
    print(min,max)
    return(min,max)

findMinAndMax([2,2,3,'haha'])
findMinAndMax([2,2,3])
findMinAndMax([2,2,3,4,5,6,7,8])
