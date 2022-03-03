# 使用 bool 内置类可以将其他数据类型转换成为布尔值
print(bool(100))  # 将数字100转换成为布尔值
print(bool(-1))  # True -1转换成为布尔值也是True
print(bool(0))  # False

# 数字里，只有数字 0 被转换成为布尔值是False，其他数字转换成为布尔值都是True

print(bool('hello'))  # True
print(bool('False'))  # True
print(bool(''))  # False
print(bool(""))  # False

# 字符串里，只有空字符串''/""可以转换成为False，其他字符串都转换成为True

# None 转换成为布尔值是False
print(bool(None))  # False
print(bool('None'))  # True

print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

# 总结，在python中，只有空字符串""/''，数字0，空列表[]，空元组()，空字典{}, 空集合set()和空数据None会被转换成为False，其他的都会被转换成为True

# 集合
# {'name': 'zhangsan', 'age': '18'}  # 字典
# {1, 2, 3, 4} # 集合
# {} # 空字典
s = set()
print(bool(s))
print(bool(set()))

# 在计算机里，True和False其实就是使用数字1和0 来保存的
print(True + 1)  # 2
print(False + 1)  # 1

# 隐式类型转换
if 0:
    print('good')
