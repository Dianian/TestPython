#
# Created by 付博文 on 2017/9/29.
#

# 函数的参数

# 位置参数

def power(x):
    return x * x


# 这里的x就是位置参数


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可以计算x的任意次方
# n为默认参数 默认值为2 可填可不填，不填时为2


# 默认参数的坑
# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end([1,2,3]))
#
# print(add_end())


# 可变参数
# 可变参数前加 *
def calc(*numbers):
    for number in numbers:
        print(number)


calc(1, 2, 3, 4, 5)
calc(456, 488)
