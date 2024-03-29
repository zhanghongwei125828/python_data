# 字符串的操作

################################################################################

# 首字母大写     -capitalize
s1 = 'true'
ss1 = s1.capitalize()
print(ss1)
# 字符串全部大写  -upper
s2 = 'zhangsan'
ss2 = s2.upper()
print(ss2)
# 字符串全部小写   -lower
s3 = 'ZHANGSAN'
ss3 = s3.lower()
print(ss3)
# 大小写翻转   -swapcase
s4 = 'ZHANGsan'
ss4 = s4.swapcase()
print(ss4)
# 每个隔开的单词首字母大写  #可以使用空格,特殊字符或者数字隔开  -title
s5 = 'zhangsan,lisi,wangwu'
ss5 = s5.title()
print(ss5)

################################################################################

#居中   -center
s6 = 'abcdefg'
ss6 = s6.center(20)
print(ss6)
#有填充物的居中
s7 = 'abcdefg'
ss7 = s7.center(20,'@')
print(ss7)

################################################################################

# 看字符长度  -len  # 公共方法 str int tuple 等都可以用
s8 = 'abcde'
ss8 = len(s8)
print(ss8)

###############################zha#################################################

# 以什么开头  -startswith        #返回True 或 False
s9 = 'sdfasfgswd'
ss9 = s9.startswith('sdf')
print(ss9)
#  以什么结尾  -endswith         #返回True 或 False
s10 = 'sdfasfgswd'
ss10 = s10.endswith('swd')
print(ss10)

################################################################################

# 通过元素找索引 - find  #找到返回索引位置    #找不到返回 -1
s11 = '1234abcd'
ss11 = s11.find('c')
print(ss11)
# 通过元素找索引 -index  #找到返回索引位置  # 找不到报错
s12 = '1234abcd'
ss12 = s12.index('d')
print(ss12)

################################################################################

# 去掉空格  -strip  --默认去掉空格

s13 = ' #sabc@ '
ss13 = s13.strip()
dl = s13.strip(' #@ ')    # 不分先后顺序  # lstrip从左删除  rstrip从右删
print(ss13)
print(dl)
# 去掉左边空格 -lstrip
sss13 = s13.lstrip()
print(sss13)
# 去掉右边空格 -rstrip
ssss13 = s13.rstrip()
print(ssss13)

################################################################################

# 输出一段字符串里面有多少同个字符

s14 = 'aabbababaa'
ss14 = s14.count('a')
print(ss14)

################################################################################

# split 分割     str ----> list
s15 = 'zhangsan,lisi,wangwu'
l1 = s15.split(',')
print(l1)

################################################################################

# format的三种用法
# 例1  按照位置 依次显示
a = ('我叫{},今年{}岁,性别{},爱好{}').format('张三','18','男','羽毛球')
print(a)
# 例2  可以随意填写顺序
b = ('我叫{0},今年{1}岁,性别{2},爱好{3}').format('张三','18','男','羽毛球')
print(b)
# 例3   填写变量
c = ('我叫{name},今年{age}岁,性别{gender},爱好{hobby}').format(hobby='羽毛球',age=18,name='张三',gender='男')
print(c)

################################################################################

# 字符串替换 replace
d = '张三,lisi,wangwu,zhangsan,张三'
dd = d.replace('张三','张二',1)
print(dd)

################################################################################

