#  使用 str 内置类可以将其他类型的数据转换成为字符串
a = 34
b = str(a)
print(a)  # 34
print(b)  # 34
print(a + 1)  # 35
# print(b + 1)  # 报错 TypeError: can only concatenate str (not "int") to str

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
