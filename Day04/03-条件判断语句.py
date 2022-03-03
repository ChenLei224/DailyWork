# python里的条件判断语句 if / if else / if elif elif else
# python里不支持 switch...case 条件语句

# if 条件判断：
#   条件成立时，执行的代码
# else:
#   条件不成立时，执行的代码


age = int(input('请输入您的年龄：'))
if age < 18:  # 字符串和数字做比较运算的规则： == 结果是False, != 结果是True，其他比较运算会报错
    print('赌博时不好的哟，好好学习，天天向上')
else:
    # if条件不满足时执行的代码
    print('澳门首家线上赌场上线了！')
