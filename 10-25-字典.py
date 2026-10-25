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
