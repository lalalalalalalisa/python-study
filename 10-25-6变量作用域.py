## 作用域
# 局部变量
def func1():
    num1 = 100
    print(f'func1里面打印num1:{num1}')
func1()
print(f'在函数外面打印num1:{num1}') # 报错

# 全局变量
num2 =100
def func2():
    global num2
    num2 = 666
    print(f'num2=666下方的打印{num2}')
func2() # num2=666下方的打印666
print(num2) # 之前是100，global之后变成666

# 变量就近原则
def func():
    print(f'第一句打印{num1}') # 报错，变量满足就近查找，当前作用域有num1，但后定义，也报错
    num1 = 20
    print(f'第二句打印{num1}')
func()

# lambda表达式
def func1():
    print('hello world')
func1()
# 匿名函数
func2 = lambda : print('hello world')
func2()

# ✅求任意两个数的和，并把结果返回
func3 = lambda x, y: x + y # 不能加return
print(func3(1, 2))

# 带if判断（三目运算）
func = lambda a, b : a if a > b else b
print(func(10, 20))

# ✅作业题：接收两个字符串，打印长度最大的，如果两个长度相等，打印所有
func = lambda x, y: print(x) if len(x) > len(y) else print(y) if len(x) < len(y) else print(x, y)
func('sdf', 'zxcv')

# ✅列表数据+字典数据排序
student_list = [
    {"name": "张三", "age": 20, "address": '南京'},
    {"name": "李四", "age": 25, "address": '北京'},
    {"name": "王五", "age": 23, "address": '上海'},
    {"name": "赵六", "age": 19, "address": '广州'},
    {"name": "田七", "age": 22, "address": '深圳'}
]
student_list.sort(key=lambda item: item['age'],reverse=True)
print(student_list)
def get_age(student_list):
    return student_list['age']
student_list.sort(key=get_age, reverse=True)
#带不带括号：
#1.不带括号，传递规则，把函数当成变量传给别人
#2.带括号，立即运行拿到结果
#lambda item: item['age']没带括号，他就是个规则，直接传值给key
