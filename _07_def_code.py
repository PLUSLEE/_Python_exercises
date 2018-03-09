#-*-coding:utf-8-*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#Pyhton交互环境下，定义函数时显示...

#---------------------------------
#参数类型检查
def my_abs_upgrade(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad Idea')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))
