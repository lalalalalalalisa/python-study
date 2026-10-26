## 元组
# # 定义
t1 = ('小红', '小明', '小强')
print(type(t1)) # <class 'tuple'>
t2 = (10,) # 只有一个数据的元组也要加逗号
t2 = (10) # 不是元组，小括号里的数据是啥类型，最终就是啥类型
print(type(t2)) # <class 'int'>

# 修改 - 元组不能修改
t1[0] = '大红' # 报错

# 和字符串同样方法
print(t1[0:2]) # ('小红', '小明')
print(len(t1)) # 3
print(t1.count('小红')) # 1

# 查找
t1 = ('小红', '小明', '小强')
print(t1.index('小红')) # 0
print(t1.index('小红666')) # 报错，不存在
print('小红' in t1) # True
print('小红' not in t1) # False

# ✅提取嵌套元组中的唯一元素
tuple1 = ((1, 2, 3), (2, 4, 6), (2, 3, 5))
new_list = []
for item in tuple1:
    for i in item:
        if i not in new_list:
            new_list.append(i)
print(new_list)

# tuple()转元组类型
t1 = tuple(new_list)
print(t1)

# ✅计算奇数的个数
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count = 0
for i in my_tuple:
    if i % 2 == 1:
        count += 1
print(count)
