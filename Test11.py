# 递归

# 在函数内部调用其它函数
# 计算阶乘
# n!=1x2x3x...xn

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 计算过程
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120


# 由于栈的大小不是无限的， 递归调用的次数过多，
# 会导致栈溢出  比如fact(1000)

# 解决栈溢出的方法是通过 尾递归 优化
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# fact(10000)

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。