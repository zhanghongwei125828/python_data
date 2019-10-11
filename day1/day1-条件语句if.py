# 条件语句

'''
if 条件:
    结果
'''
################################################################################

# 案例1   单条件判断
'''
if True:
    print(123)
print(456)       # 此判断条件打印123就已经截止了,print(456)不在判断条件里,注意缩进
'''
################################################################################

# 案例2   if else 如果满足条件就怎么样否则怎么样
'''
if 100 > 99:
    print(666)
else:
    print(555)
'''
################################################################################

# 案例3   多条件判断
'''
num = int(input('请输入一个数字:  '))
if num == 1:
    print('num == 1')
elif num == 2:
    print('num == 2')
elif num == 3:
    print('num == 3')
else:
    print("您输入的都不正确")
'''
################################################################################

# 案例4   if嵌套
'''
name = input('请输入你的名字: ')
age = int(input('您的年龄: '))
if name == 'zhangsan':
    if age == 18:
        print('hello,zhangsan')
else:
    print('您输入的不正确')
'''

