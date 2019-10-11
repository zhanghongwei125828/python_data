# while 循环

'''
while True:

'''

################################################################################
# 示例1   循环1至100
'''
count = 0
while count <= 100:
    print(count)
    count += 1
'''
################################################################################

# 示例2
'''
count = 1
while count <= 3:
    name = input("请输入您的姓名: ")
    pwd = input("请输入您的密码: ")
    count += 1
    if name == 'zhangsan':
        if pwd == 'abc123':
            print("你好啊张三")
            break
    else:
        print("您输入的用户名或密码不正确，请重新输入")
        continue
'''




