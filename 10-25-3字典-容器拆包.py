## 字典
dict1 = {'name': 'daqiu', 'age': 18, 'gender': '女'}
dict2 = {} # 空字典
dict2 = dict() # 空字典

# 查
print(dict1['name'])
# 获取所有key
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
for key in dict1.keys():
    print(key)
    print(dict1[key])
# 获取所有值
print(dict1.values()) # dict_values(['daqiu', 18, '女'])
for v in dict1.values():
    print(v)
# 获取所有键值对 - 键值对组合成元组，不可修改
print(dict1.items()) # dict_items([('name', 'daqiu'), ('age', 18), ('gender', '女')])
for item in dict1.items():
    print(item) # ('name', 'daqiu') ('age', 18) ('gender', '女')
    print(item[0], item[1])

# 新增和修改
dict1 = {'name': '小红', 'age': 18, 'gender': '女'}
# 修改 字典是可变数据类型
dict1['age'] = 20
# 新增
dict1['address'] = '北京市顺义区' # 新增
dict1['address'] = '北京市昌平区' # 修改

# 删除和清空
dict1 = {'name': '小红', 'age': 18, 'gender': '女'}
# 删除某个键值对
del dict1['gender']
# 清空某个字典
dict1.clear() # clear()返回None


# ✅统计字符串中每个字母出现的次数 返回字典
str1 = 'abcdacdae'
dict1 = {}
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1) # {'a': 3, 'b': 1, 'c': 2, 'd': 2, 'e': 1}

# ✅字符串切割为字典 '5=five 6=six 7=seven'
str1 = '5=five 6=six 7=seven'
list1 = str1.split(' ') # 一定要是空格，返回一个列表
print(list1) # ['5=five', '6=six', '7=seven']
dict1 = {}
for i in list1:
    # print(i.split('=')) ['5', 'five']
    list2 = i.split('=')
    dict1[list2[0]] = list2[1]
print(dict1) # {'5': 'five', '6': 'six', '7': 'seven'}

## 容器拆包 又叫解包
t1 = (10, 20, 30, 40)
num1, num2, num3, num4 = t1
print(num1, num2, num3, num4)
list1 = ['张三', '李四']
a, b =list1
print(a, b)

# ✅字符串切割为字典 '5=five 6=six 7=seven'
str1 = '5=five 6=six 7=seven'
list1 = str1.split(' ') # 一定要是空格，返回一个列表
print(list1) # ['5=five', '6=six', '7=seven']
dict1 = {}
for i in list1:
    # print(i.split('=')) ['5', 'five']
    a, b = i.split('=')
    # print(a, b)  # 5 five
    dict1[a] = b
print(dict1) # {'5': 'five', '6': 'six', '7': 'seven'}



