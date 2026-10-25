## 集合set
s1 = {1, 10, 5, 7, '小强', 10}
# 无序 去重
# 因为集合无序，所以没有索引
s2 = set() # 定义空集合
s3 = {}    # 定义空字典dict

# 增删查
s1 = {1, 10, 5, 7, '小强', 10}

# 集合是可变数据类型
# for 遍历   不能用while遍历：因为集合是无序的，不能用索引找
for item in s1:
    print(item)

# 新增数据
s1.add('小红')
s1.add(10)
if '小红' not in s1:
    s1.add('小红')

# 删除数据
s1.remove('小强')

# ✅统计缺失数据和
numbers = [2, 5, 3, 7, 5, 7]
min_num = min(numbers)
max_num = max(numbers)
s1 = set(numbers) # 集合没有重复数据，减少判断次数
sum = 0
for i in range(min_num + 1, max_num):
    if i not in s1:
        sum += i
print(sum)
