# python里可以使用一层循环直接打印三角形
# i = 0
# while i < 5:
#     i += 1
#     print(i * "*")

# 总结：外循环用来控制行数，内循环用来控制每一行的列数
# 这一大段代码，是用来打印五行五裂星星的
j = 0
while j < 5:
    j += 1

    # 本段代码是打印五个星星并且换行
    i = 0
    while i < 5:
        i += 1
        print("*", end="  ")  # 打印一个星星，不换行
    print()  # 用来换行




# print("*", end="  ")
# print("*", end="  ")
# print("*", end="  ")
# print("*", end="  ")
# print("*", end="  ")
# print()

