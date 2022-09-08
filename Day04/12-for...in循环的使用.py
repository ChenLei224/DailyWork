# python里的for循环指的是for...in循环。和c语言里的for不一样
# for语言格式： for ele in iterable
# for i in [1, 2, 3, 4, 5, 6, 7,8, 9, 10]:
#     print(i)

# range 内置类用来生成指定区间的整数序列
# 注意：in 的后面必须是一个可迭代对象！！！
# 目前接触的可迭代对象：字符串、列表、字典、元组、集合、range
# for i in range(0, 10):
#     print(i)

# for x in [1, 2, 3, 4, 5, 7, 8, 9, 10]
#     print(x)

# for y in "hello":
#     print(y)

# for m in 10:  # in的后面必须是一个可迭代对象
#     print(m)

z = 0  # 定义一个变量用来保存所有数字之和
for i in range(1, 101):
    z = z + i
print(z)
