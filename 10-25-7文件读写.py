## 文件读写
# 打开
f = open('data.txt', 'r', encoding='utf-8')
# 读取
print(f.read())
# 关闭
f.close()

# 找文件路径
# 1.py和txt在同一个文件夹：直接写文件名.后缀
# 2.txt在py下一级：文件夹名/目标文件.后缀
# 3.txt在py上一级：../目标文件.后缀   # ../一次往上退一级文件夹

# 三种核心打开方式
f = open('data.txt', 'r', encoding='utf-8') # 只读
f = open('data.txt', 'w', encoding='utf-8') # 覆盖写入，只写
f = open('data.txt', 'a', encoding='utf-8') # 追加写入，没有文件则创建文件
print(f.read())
f.write('hi python')
f.close()

# 读取
f = open('data.txt', 'r', encoding='utf-8')
print(f.read()) # 读取所有内容
print(f.read(7)) # 读取指定长度
list1 = f.readlines()  # ['你好呀大秋\n', 'hi\n', 'python\n', 'hi\n', 'python']
                       # 读取所有，返回列表，列表的每个数据是一行内容，包含\n
f.seek(0) # 改变文件读取的开始位置 -> 0表示文件开头 -> 文件指针
print(f.readline()) # 读取一行
print(f.readline()) # 读取一行
f.close() # 关闭

# 循环读取
f = open('data.txt', 'r', encoding='utf-8')
while True:
    data = f.readline()
    if not data:
        break
    print(data, end='')
f.close()

## with open()文件读写
# 不用再关，自己会关闭
with open('data.txt', 'r+', encoding='utf-8') as f:
    print(f.read())
    f.write('你好世界')

# ✅复制视频文件
# 不能加encoding='utf-8'，这是二进制
with open('aa/04-函数-基础参数汇总.mp4', 'rb') as src_f, open('aa/04-beifen.mp4', 'wb') as new_f:
    while True:
        data = src_f.read(1024)
        if not data:
            break
        # print(data)
        new_f.write(data)

# ✅反转文件内容
with open('aa/a.txt', 'r', encoding='utf-8') as src_f, open('aa/c.txt', 'w', encoding='utf-8') as new_f:
    while True:
        data = src_f.readline()
        if not data:
            break
        data = data.replace('\n', '')
        reverse_data = data[::-1]
        new_data = reverse_data + '\n'
        # print(data)
        new_f.write(new_data)
