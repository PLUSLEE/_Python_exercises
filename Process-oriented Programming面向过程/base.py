'''
单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

引入errors，忽略
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'''

x = chr(25991)
y = 'ABC'.encode('ascii')
z = '毛毛2.4G'.encode('utf-8')

x1 = b'\xe6\xaf\x9b\xe6\xaf\x9b2.4G'.decode('utf-8')

print(x,y,z)
print(x1)
