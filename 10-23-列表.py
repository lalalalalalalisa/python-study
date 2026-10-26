## 列表
list1 = ['小红', '小明', '小强']
list2 = []
list2 = list()
print(list2, type(list2))

# 索引与切片
print(list1[0]) # 小红
print(list1[-1]) # 小强
print(list1[0:2]) # ['小红', '小明']
print(list1[0:20]) # ['小红', '小明', '小强']
print(list1[200]) # 报错 list index out of range 下标越界

# 遍历
list1 = ['小红', '小明', '小强', 'Rose', 'Jack']
# for遍历
for i in list1:
    print(i)
# 拓展 while遍历
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# # 查
list1 = ['小红', '小明', '小强', 'Rose', 'Jack', '小强']
print(list1.index('小强')) # 2
print(list1.index('小强666')) # 报错  '小强666' is not in list
print(list1.count('小强')) # 2
print('小强' in list1)
print('小强' not in list1)

# 增
list1 = ['小红', '小明', '小强']
# append 整体追加
list1.append('Jack') # 改变的是原数据
list1.append(['aa', 'bb']) # ['小红', '小明', '小强', 'Jack', ['aa', 'bb']]
print(list1[4][0]) # aa
# extend 逐项增加-容器拆开再追加
list1.extend(['aa', 'bb']) # ['小红', '小明', '小强', 'aa', 'bb']
list1.extend('daqiu') # ['小红', '小明', '小强', 'd', 'a', 'q', 'i', 'u']
print(list1)
# # insert 任意位置增加
list1.insert(1, 'cc')

# 删
list1 = ['小红', '小明', '小强']
# del 删除
del list1
print(list1) # name 'list1' is not defined.
del list1[0]
print(list1) # ['小明', '小强']
# pop（索引）：默认删除最后一个数据，如果定制了索引就删除这个索引对应的数据
del_name = list1.pop() # 小强
del_name = list1.pop(1) # 小明
print(f'恭喜，已经删除了{del_name}')
# remove(数据)
list1.remove('小强') # ['小红', '小明']
print(list1)

# 改
list1 = ['小红', '小明', '小强']
# list[i] 按下标修改数据
list1[0] = '大红'
list1[10] = '大红' # 报错，下标越界
# reverse()反转
list1.reverse() # ['小强', '小明', '小红']
print(list1)
# sort()
list2 = [10, 3, 4, 2, 6, 7, 2, 5]
list2.sort()
print(list2)
print(list2.sort()) # None
list2.sort(reverse=True) #降序：反转吗 -> 反转
print(list2)

# 嵌套列表
stu_name = [
    ['张三', '李四', '王五'],
    ['Rose', 'Jack', 'Lily']
]
print(stu_name[1][1]) # Jack
# 嵌套列表的遍历
for item in stu_name:
    # print(item) # ['张三', '李四', '王五'] ['Rose', 'Jack', 'Lily']
    for i in item:
        print(i)

# 求相邻元素最大值
list1 = [7, 8, 9, 5, 6, 7, 2, 3]
new_list = []
for i in range(0, len(list1)-1):
    if list1[i] > list1[i+1]:
        new_list.append(list1[i])
    else:
        new_list.append(list1[i+1])
print(new_list) # [8, 9, 9, 6, 7, 7, 3]
