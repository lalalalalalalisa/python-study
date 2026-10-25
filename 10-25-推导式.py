## 推导式
# 列表推导式
list2 = [i for i in range(1, 11)]
# 集合推导式
s1 = {i for i in range(1, 11)}
# 字典推导式
dict1 = {i: i*2 for i in range(1, 11)}
print(dict1) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}
# 元组没有推导式
# 注意：这不是元组，是生成器（generator)--就业班学
t1 = (i for i in range(1, 11))
print(t1, type(t1))

# for 循环嵌套列表推导式
# for - if
list3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list3.append(i)
print(list3) # [2, 4, 6, 8, 10]

list4 = [i for i in range(1, 11) if i % 2 == 0]
print(list4)
# for - for
# 外层循环两次，内层循环三次
list5 = [(i, j) for i in range(1, 3) for j in range(0, 3)]
print(list5) # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
