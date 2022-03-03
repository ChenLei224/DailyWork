# python里的数据类型：
# 整型(int)
# 浮点型(float)
# 复数(complex)
# 字符串类型(string)
# 布尔类型(bool)
# 列表(list)
# 字典(dict)
# 元组(tuple)
# 集合(set)

# 整型就是整数。 计算机其实只能保存二进制 0 和 1， 为了方便数据的表示，同时计算机也支持八进制和十六进制
# 二进制 八进制 十六进制 十进制 在python里都能够表示

a = 98  # 默认数字都是十进制的数字。 98就是十进制的九十八
b = 0b101101101  # 以0b开头的数字是二进制
print(b)  # 当使用print语句打印一个数字的时候，默认也是使用十进制打印输出的

# c = 0b121010102 # 二进制里最大的数字是1， 不能出现2

c = 0o34  # 以0o开头的数字是八进制的数字
print(c)  # 28
# x = 0o79  # 八进制里最大的个位数是7

# 十六进制 0～9 a~f
d = 0x23  # 以0x开头的数字是十六进制的数字
print(d)  # 35

d = 0x2a
print(d)  # 42

# m = 045
# print(m)  # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
