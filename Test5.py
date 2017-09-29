#
# Created by 付博文 on 2017/9/29.
#

# 条件判断

# if
age = 20
if age >= 18:
    print("你的年龄是", age)
    print('成年人')

# if else
age = 3
if age > 18:
    print("你的年龄是", age)
    print('成年人')
else:
    print("你的年龄是", age)
    print('未成年人')

# elif
age = 3
if age > 18:
    print('成年人')
elif age >= 6:
    print("未成年人")
else:
    print('小孩')

# 判断条件简写 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 1
if x:
    print(True)

# input
birth = input('请输入年份：')
s = int(birth)
if s < 2000:
    print('00前')
else:
    print('00后')
