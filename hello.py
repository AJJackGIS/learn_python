import keyword
import sys

print("hello")

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

if True:
    print("true")
else:
    print("false")

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以有多行组成"""

str = '123456789'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串
print('------------------------------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

print(list(range(10)))

listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)

dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)

a = (x for x in range(1, 10))
print(tuple(a))

print(10 / 3)
print(10 // 3)
print("\a")

a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a + b

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
for x in it:
    print(x)


def max_value(left, right):
    if left > right:
        return left
    else:
        return right


a = 14
b = 15
print(max_value(a, b))
