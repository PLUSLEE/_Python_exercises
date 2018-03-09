'''

练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi <= 18.5:
    print("过轻")
elif bmi > 18.5 and bmi <= 25:
    print("正常")
elif bmi >25 and bmi <= 28:
    print("过重")
elif bmi >28 and bmi <= 32:
    print("肥胖")
else:
    print("严重肥胖")

#---------------------------------------------
#Python支持直接进行比较，区别于Java
h=height
w=weight
bmi=w/(h*h)
if bmi<18.5:
    print('过轻')
elif 18.5<bmi<=25:
    print('正常')
elif 25<bmi<=28:
    print('过重')
elif 28<bmi<=32:
    print('肥胖')
elif 32<bmi:
    print('严重肥胖')


#---------------------------------------------
#另外一种看着比较有趣的方法
h=1.75
w=80.5
bmi=w/(h*h)
if bmi>=18.5:
    if bmi>=25:
        if bmi>=28:
            if bmi>=32:
                if bmi > 32:
                    print("严重肥胖")
            else:
                print("身材肥胖")
        else:
            print("身材过重")
    else:
        print("身材正常")
else:
    print("身材过轻")
