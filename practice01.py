"""
@Description : 
@Author      : Su Jingpeng
@Copyright   : 杭州中为光电技术有限公司
@Date        : 2022-03-11 13:40:31
@LastEditors : Su Jingpeng
@LastEditTime: 2022-03-14 09:26:59
@Modified    : 
"""

# split()
# str = 'hello_world_yoyo'
# print(str.split("_"))

# join()
# str = ['hello', 'world', 'yoyo']
# print("_".join(str))

# str = ['hello', 'world', 'yoyo']
# re = ''
# for i in range(2):
#     str[i] = str[i] + '_'
# for j in str:
#     re = re + j
# print(re)

# replace('', '')
# s = 'python is a good language!'
# print(s.replace(' ', '%20'))

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}\t'.format(i, j, i * j), end='')
#     print()

# while True:
#     x = input("请输入第一个数字：")
#     y = input("请输入第二个数字：")

#     try:
#         sum = float(x) + float(y)
#     except ValueError:
#         print("输入错误，请重新输入！")
#         continue
#     else:
#         print('两数和为：{0:.2f}'.format(sum))
#         break

x = int(input("请输入范围："))
for num in range(x):
    n = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if num == sum:
        print(num, end=' ')
