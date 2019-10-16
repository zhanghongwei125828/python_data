# 字符串的操作

# 首字母大写
s1 = 'true'
ss1 = s1.capitalize()
print(ss1)

# 字符串全部大写
s2 = 'zhangsan'
ss2 = s2.upper()
print(ss2)

# 字符串全部小写
s3 = 'ZHANGSAN'
ss3 = s3.lower()
print(ss3)

# 大小写翻转
s4 = 'ZHANGsan'
ss4 = s4.swapcase()
print(ss4)

# 每个隔开的单词首字母大写  #可以使用空格,特殊字符或者数字隔开
s5 = 'zhangsan,lisi,wangwu'
ss5 = s5.title()
print(ss5)

#居中
s6 = 'abcdefg'
ss6 = s6.center(20)
print(ss6)
#有填充物的居中
s7 = 'abcdefg'
ss7 = s7.center(20,'@')
print(ss7)

# 看字符长度   # 公共方法 str int tuple 等都可以用
s8 = 'abcde'
ss8 = len(s8)
print(ss8)

# 以什么开头
s9 = 'sdfasfgswd'
ss9 = s9.startswith('sdf')
print(ss9)