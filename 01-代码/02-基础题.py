# 根据输入的百分制成绩打印"及格"或者"不及格"，60分以下为不及格
# 1.使用input接收用户的输入内容
# 2。使用float内置类，将接收到的字符串转换成为浮点数
# score = float(input("请输入您的成绩："))
# # 3.使用一个if...else语句来判断用户是否及格
# if score >= 60:
#     print("恭喜你，及格了")
# else:
#     print("没及格")

# 根据输入的年龄打印"成年"或者"未成年"，18岁以下为未成年，如果年龄不在正常范围（0到150岁）内侧打印"这不是人！"
# age = int(input("请输入你的年龄："))
# if 150 >= age >= 0:
#     if age < 18:
#         print("未成年")
#     else:
#         print("成年人")
# else:
#     print("这不是人")

# 输入两个整数，如果两个数相减的结果为奇数则输出该结果，否则输出提示信息"结果不是奇数"
# 一个input接收一次用户的输入，如果想要接收多次用户的输入，使用多个input
# num1 = int(input("请输入一个整数"))
# num2 = int(input("请输入一个整数"))
# result = num1 - num2
# if result % 2 == 0:
#     print("结果不是奇数")
# else:
#     print(result)

# 使用for循环输出0到100内所有的奇数
# for i in range(0, 101):
#     if i % 2 == 0:
#         continue
#     print(i)

# 使用while循环输出0到100内所有的偶数
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

