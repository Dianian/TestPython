# 函数式编程
# 函数式编程的一个特点就是，
# 允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# Python对函数式编程提供部分支持。
# 由于Python允许使用变量，因此，Python不是纯函数式编程语言


# 高阶函数 一个函数可以接受另一个函数作为参数我们称之为高阶函数

# 函数本身也可以赋予变量

# f = abs
# print(f(-10))

# 函数名也可以是变量

# abs = 10
# abs(-10)  报错  不允许这样写

# abs指向10后，就无法通过abs(-10)调用该函数了


# 传入函数


def add(x, y, f):
    return f(x) + f(y)


print(add(-10, 5, abs))


# 高阶函数，就是让函数的参数能够接收别的函数。


# map / reduce
# Python内建了map()和reduce()函数。

# map 传入两个参数 一个是函数，一个是iterable（可迭代对象）
# map 将传入的函数依次作用到序列的每一个元素，
# 并把结果作为新的 iterator （迭代器） 返回

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

# reduce 把函数作用在 [x1,x2,x3,^] 上，这个函数必须接收两个参数，
# reduce 把结果继续和序列的下一个元素做累计运算
from functools import reduce


# 例子 求和函数
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))


# 求和函数可以用Python内建的sum求和函数 ，没必要用 reduce

# 把序列 [1,3,5,7,9] 变换成整数 13579

def fu(x, y):
    return x * 10 + y


print(reduce(fu, [1, 3, 5, 7, 9]))


# filter 用于过滤序列
# 接收一个函数 和 一个序列
# 把传入的函数依次作用于每一个元素 ，然后跟据传入函数的的返回值是 True 还是 False 决定是保留该函数还是丢弃该函数

# 例子 在一个 list 中 删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

###小记 忘了转换 list




# sorted 排序

# 使用 sorted 对list 进行排序

print(sorted([36, 5, -12, 9, -21]))

# 还可以接收一个 key 根据key返回的结果进行排序
# 按绝对值的大小进行排序

print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 字符串排序，是按照ASCII的大小比较的，
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

# 传入key 实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 进行反向排序 传入第三个参数 reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
