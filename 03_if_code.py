#-*-coding:utf-8-*-

age = 20
if age >=18:
    print("your age is:",age)
    print("adult")

age = 3
if age>=18:
    print("your age is:",age)
    print("adult")
else:
    print("your age is:",age)
    print("teenager")

age = 3
if age>=18:
    print("adult")
elif age >= 6:
    print("teenager")
else :
    print("kid")


#if 判断条件简写
#只要判断条件是非零数值，非零字符串，非空list等，均判断为true
x = 1
if x:
    print("True")
else:
    print("False")


#input方法的使用
birth = int(input("birth day:"))

if birth >=2000:
    print("00后")
else:
    print("00前")
