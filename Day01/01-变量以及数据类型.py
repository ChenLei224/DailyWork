# a 我们就称之为变量。使用一个名字，代替一段内容
a = '你好世界'
print(a)

b = 34
print(b)

c = True
print(c)

# 数据类型的概念：
# 在python里数据都有各自对应的类型：
# int 整数类型

# 数字类型： 整数型int 浮点型float 复数complex
print(45 + 1)  # int整数类型
print(3.1415)  # float浮点类型
print((-1) ** 0.5)  # complex复数类型

# 字符串类型： 其实就是一段普通的文字
# python里的字符串要求使用一对单引号，或者双引号来包裹
print('今天天气好晴朗，处处好风光呀好风光')
print('56')

# 布尔类型： 用来表示 真假/对错
# 布尔类型里一共只有两个值，一个是True，一个是False
print(4 > 3)  # True
print(1 > 5)  # False
print(True)
print(False)

# 列表类型
names = ['姚万万', '邹碧慧', '郑美水', '蔡顺利', '李想', '蔡徐坤']

# 字典类型
person = {'name': '袁奋', 'age': 18, 'addr': '湖北', '身高': '180cm'}

# 元祖类型
nums = (1, 8, 9, 2, 3, 0)

# 集合类型
x = {9, 'hello', 'hi', 'good', True}
