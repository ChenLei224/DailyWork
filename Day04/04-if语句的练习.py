# 写出判断一个数是否能同时被4和6整除的条件语句，并且打印对应的结果
#num = int(input('请输入一个数字：'))

# if num % 4 == 0 and num % 6 == 0:
#     print('能够被4和6同时整除')
# else:
#     print('不能被4和6同时整除')


# 写出判断一个数是否能被3或者7整除，但是不能同时被3和7整除的条件语句，并且打印对应的结果
# if (num % 3 == 0 or num % 7 == 0) and (num % 21 != 0):
#     print('能被3或者7整除，但是不能同时被3和7整除')
# else:
#     print('不满足条件的数字')


# 输入年，写代码判断输入的年是否是闰年，并且打印对应的结果。（是闰年的条件：能被4整除但是不能被100整除或者能够被400整除）
# year = int(input('请输入一个年份：'))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, '是闰年')
# else:
#     print(year, '不是闰年')


# 假设今天的上课时间为15678秒，编程计算今天上课时间是多少小时，多少分钟，多少秒；以'XX时XX分XX秒'的方式表示出来
# 3718 ==> 1小时3600 118秒 1分钟60 58秒
# x = 3718
# hour = x // 3600
# minute = x % 3600 // 60
# second = x % 60
# print(hour, '小时', minute, '分钟', second, '秒')


# 定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常！
# 公式： 体重(kg)/身高(m)的平方值在18.5~24.9之间属于正常
height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
# BMI = weight/(height*height)
BMI = weight / height ** 2
if 18.5 <= BMI <= 24.9:
    print('您的身材正常')
else:
    print('您的身材异常')
