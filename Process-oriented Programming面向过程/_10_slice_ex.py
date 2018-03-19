#-*-coding:utf-8-*-
'''
利用切片操作，实现一个trim()函数，
去除字符串首尾的空格，注意不要调用str的strip()方法：

'''
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    print(s)
    return s

#if判断+递归循环优化结果
def trim_up(s):
    if s == '':
        return s
    elif s[0] ==' ':
        return trim_up(s[1:])
    elif s[-1] == ' ':
        return trim_up(s[:-1])
    else:
        print(s)
        return s

trim('   haha')
trim('   haha    ')
trim('')
trim('  ')


trim_up('   haha')
trim_up('   haha    ')
trim_up('')
trim_up('  ')

'''
总结：当看到别的代码时，感觉自己写的就是一坨屎
想到循环，但是只能想到for循环，忘记了while这个大利器
'''
