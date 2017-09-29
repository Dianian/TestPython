#
# Created by 付博文 on 2017/9/29.
#

# 循环


# for...in 循环
names = ['Admin', 'Bob', 'Jack']
for name in names:
    print(name)
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

# 计算1-10之间的整数
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
print(sum)

# 计算1-100的整数之和，
# range()函数可以生成一个整数序列
# 在通过list()函数可以转换为list

print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
# 在循环中break语句可以提前退出循环

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue 在循环过程中 通过continue语句跳过当前的循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue
    print(n)


#
