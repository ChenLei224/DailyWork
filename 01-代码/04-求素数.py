# 统计101-200中素数的个数，并且输出所有的素数。（素数又叫质数，就是只能被1和它本身整除的数）

for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            print(i, "是合数")
            break  # break放在内循环里，用来结束内循环
        else:
            print(i, "是质数")
