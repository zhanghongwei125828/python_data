# for循环 有限循环

s1 = 'ABCDEFG'
for i in s1:
    print(i)

#ab12cd34ef56        # 找到字符串中有几对整数
info = input('>>>')
for x in info:
    if x.isalpha():
        info = info.replace(x,' ')
l = info.split()
print(len(l))
