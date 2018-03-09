#-*-coding:utf-8-*-

#注意事项，py文件不能以数字开头
from _07_def_code import my_abs,my_abs_upgrade
print(my_abs(-10))
print(my_abs_upgrade(-11))
print(my_abs_upgrade('100pp'))


#空函数的作用：让程序继续运行下去，却不进行什么操作
def nop():
    pass    #pass语句什么都不做


#Python可以返回多个值，但那只是假象，实际上返回的是tuple
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
