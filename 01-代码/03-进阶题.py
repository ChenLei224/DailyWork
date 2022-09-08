# 使用循环计算出1到100求和的结果
# result = 0
# i = 0
# while i < 100:
#     i += 1
#     result += i
# print(result)

# result = 0
# for i in range(0, 101):
#     result += i
# print(result)


# 统计100以内个位数是2并且能够被3整除的数的个数
# count = 0
# for i in range(1, 101):
#     if i % 10 == 2 and i % 3 == 0:
#         count += 1
#         print(i)
# print("满足条件的个数有：", count, "个")


# 输入任意一个正整数，求它是几位数
# num = int(input("请输入任意一个正整数："))
# count = 0
# while True:
#     num //= 10
#     count += 1
#     if num == 0:
#         break
#     print(num)
# print("您输入的数字是", count, "位数")


# 打印所有的水仙花数
# for i in range(100, 1000):  # 456除以10，商是45，余数是6
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     if ge ** 3 + shi ** 3 + bai ** 3 == i:
#         print(i)


# 写一个程序可以不断的输入内容，如果输入的内容是exit，打印"程序结束"后结束该程序
while True:
    content = input("请输入内容：")
    if content == "exit":
        print("程序结束")
        break
