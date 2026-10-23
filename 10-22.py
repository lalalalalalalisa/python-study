## 字符串

# 定义
name = 'zhangsan'
address = '北京市顺义区'
str1 = """
hello world
你好 世界
"""
str2 = '鲁迅说：“我没说话那话”'
str2 = "鲁迅说\“我没说话那话\”"

# 索引
str1 = 'itheima'
print(len(str1))  # 7
# 开始索引是0，结束索引是 len(str1)-1
print(str1[0])
print(str1[1])
print(str1[-1])
print(str1[-2])

# 切片
# 序列名[开始位置下标:结束位置下标:步长] 顾头不顾尾 默认步长为1 
str1 = '0123456789'
str1[1:7:1] # 123456
str1[1:7:2] # 135
str1[1:7]   # 123456
str1[:7]    # 0123456
str1[1:]    # 123456789
str1[::]    # 0123456789
str1[::-1]  # 9876543210
str1[2:6:-1] # 报错

img_str = 'avatar.png'
img_str[:6] # avatar
img_str[6:] # .png
new_img = img_str[:6] + '-副本' + img_str[6:]

# 查找
str1 = 'hello world'
str1.find('e')  # 返回下标 1
str1.find('1e') # 没有找到 返回-1
str1.rfind('l') # 从右往找
str1.index('e') # 1
str1.index('1e') # 报错：未找到字符串

# in not in
print('o' in str1) # True
print('c' not in str1) # True

# count
print(str1.count('l')) # 3
print(str1.count('c')) # 0

# 修改
str1 = 'hello world hello python'
# replace(old, new, 次数)
str1.replace('hello', 'hi', 1) # hi world hello python
str1.replace('hello', 'hi')    # 全部替换 hello world hello python

# split(分隔符)
str1.split(' ') # ['hello', 'world', 'hello', 'python']
str1.split('@') # ['hello world hello python'] 
str1.split('')  # 报错,空分隔符

# '连接符'.join(序列) 把列表拼接成字符串






