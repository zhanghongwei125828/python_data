# 数据类型转换

# int ----> str
'''
a = 10
s = str(a)
'''

# str ----> int  # ps:  str转int str必须是数字
'''
b = '123'
i = int(b)
'''

# int ----> bool  # 0是False  非0就是True
'''
c = 3
b = bool(c)
'''

# bool ----> int   # 0是False  1是True   ps: while循环 while Ture: 等同于 while 1:  while 1效率更高
'''
d = True
e = False
i = int(d)
i1 = int(e)
print(i)
print(i1)
'''

# str ----> bool  # ''中为空字符串就是False 有字符串就是True
'''
s = "abc"
ss = ""
b = bool(s)
bb = bool(ss)
print(b,bb)

'''

