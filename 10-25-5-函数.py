## 函数
def func():
    print('欢迎登陆')
    print('开始游戏')
    print('结束游戏')
func()
# 160行
func()

## 参数
def get_sum(x, y): # 形参
    res = x + y
    print(res)
get_sum(1, 2) # 实参

# 位置参数
# 形参和实参 个数 位置 统一的叫位置参数
def func(name, age):
    print(f'我的名字是{name},今年{age}岁了')
func('大秋',18)

# 关键字参数
def func(name, age, gender):
    print(f'我的名字是{name}，今年{age}岁了，性别是{gender}')
func(gender='男', name='张三', age=18) # 可以不按顺序
func('李四', 19, gender='女') # 混用，关键字参数要放最后
func('李四', gender='女', 20) # 报错

# 缺省参数（默认值）
def func(name, age, gender='男'):
    print(f'我的名字是{name}，今年{age}岁了，性别是{gender}')
func('小明', 20)
func('小红', 19, '女')

### 不定长参数（可变参数）
# 不定长位置参数 *args
# 包裹位置参数，底层是元组，对传递参数有顺序要求
def func(name, age, *args):
    print(f'姓名是{name}，年龄是{age}')
    print(args) # (160, 170, 180) 放到一个元组容器中
    sum = 0
    for i in args:
        sum += i
    print(sum) # 510
func('小红', 20, 160, 170, 180)

# 不定长关键字参数 **kwargs
# 包裹关键字参数，底层是元组，对传递参数没有顺序要求
def func(name, age, **kwargs):
    print(f'姓名是{name}，年龄是{age}')
    print(kwargs) # {'id': 110, 'address': '北京市顺义区'}
    print(kwargs.keys()) # dict_keys(['id', 'address'])
    print(kwargs.values()) # dict_values([110, '北京市顺义区'])
    print(kwargs.items()) # dict_items([('id', 110), ('address', '北京市顺义区')])
func(name='xiaoming', age=20, id=110, address='北京市顺义区')

# 参数顺序
# 位置参数-关键字参数-缺省参数-不定长参数-不定长关键字参数
def func(name, age, id, gender='男', *args, **kwargs):
    pass
# 默认参数传递数据放到关键字后面的参数，也要用关键字的写法
func('xiaohong', 20, id=110, gender='女')
func('xiaohong', 20, id=110, gender='女', 10, 20) # 报错，位置参数不能出现在关键字参数后面
func('xiaohong', 20, id=110, gender='女', a=10, b=20, c=30) # **kwargs放最后

# return
def func():
    res = 10 + 20
    return res
    print('我是return下面的打印') # 不执行
num = func()
print(num) # 30
print(res) # 报错，默认无法把函数那的结果拿到函数外使用，找不到res变量

print('1234'.replace('1', '6')) # 6234 返回值是字符串
list1 = [1, 2, 3]
print(list1.append(666)) # None没有返回值

# 多返回值
def func():
    return 10, 20, 30
print(func()) # (10, 20, 30)
t1 = func() # 组包成一个元组

## 函数的嵌套使用
# 嵌套调用执行顺序：遇到函数调用，回到函数定义的位置开始执行代码
def funcA():
    print('funcA 开始的位置 ---------')
    print('funcA')
    print('funcA 结束的位置 ---------')
def funcB():
    print('funcB 开始的位置 ---------')
    funcA()
    print('funcB 结束的位置 ---------')
funcB()

# ✅计算奇数和偶数的累加和
# 接受一个数字序列，计算奇数和偶数的累加和，并返回
def get_sum(my_list):
    sum1 = 0
    sum2 = 0
    for i in my_list:
        if i % 2 == 0:
            sum1 += i
        else:
            sum2 += i
    return sum1, sum2

num_list = [i for i in range(1, 101)]
a, b= get_sum(num_list)
print(f'奇数和是{a},偶数和是{b}')
