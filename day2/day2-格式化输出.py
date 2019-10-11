# 格式化输出

# % - 占位符
# %s - str字符串占位
# %d int数字类型占位
# %% 单纯显示%

'''
name = input('请输入姓名: ')
age = input("请输入年龄: ")
height = input("请输入身高: ")
msg = "我叫%s , 今年%s岁了 ,我的身高是%s" %(name,age,height)
print(msg)
'''


# 循环进阶,格式化输出
'''
count = 1
while count < 4:
    username = input('请输入用户名')
    password = input('请输入密码: ')
    if username == 'zhangsan' and password == 'abc123!':
        print('欢迎张三登陆'); break
    else:
        if (3 - count) == 0: break
        print('您的用户名或密码不正确,请重新输入,还有%d次机会'%(3-count))
    count += 1
'''
aa

