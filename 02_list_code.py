#-*-coding:utf-8-*-
'''
对于List集合进行学习
classmate就是一个集合，其中len可以对集合进行长度计算
集合的索引和Java相同，从0开始
注意数组越界异常IndexError
'''

def showAnswer(classmate):
    lc = len(classmate)
    print(classmate,'合计人数',lc)

classmate = ["Lee",'CFF','LZ']
showAnswer(classmate)
print("直接获取最后一位的元素",classmate[-1])

classmate.append("haha")
showAnswer(classmate)

classmate.insert(0,"0我添加在了第一位")
showAnswer(classmate)

#默认推出集合中最后一位的数据
classmate.pop()
showAnswer(classmate)

#替换list中的某个元素
classmate[0] = "liuzhu"
showAnswer(classmate)

# for i in classmate:
#     print()

#-----------------------------------------
#tuple的使用
'''
tuple是另外一种有序列表，只是它不能改变
其实是他的指向不会改变
如果想要保持所有元素都不会改变，必须保证每一个元素都是不能改变的
此集合用()包含所有元素
'''

t = (1,2,4)
showAnswer(t)

#这里将集合[1,2]视为一个整体，是一个元素，输出的集合长度是3
t = (4,6,[1,2])
t[2][0] = 4
t[2][1] = 8
showAnswer(t)
