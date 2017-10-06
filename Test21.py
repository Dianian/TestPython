# 偏函数

# 设定函数参数的默认值，可以降低函数调用的难度。偏函数也可以做到这一点

# 用 int 把字符串转换为整数，默认是十进制
import functools

print(int('12345'))

# 可以使用 int 额外提供的 base参数 ，可以实现N进制的转换

print(int('12345', base=8))  # 8 进制
print(int('12345', 16))  # 16 进制


# 定义一个默认转换2进制的函数
def int2(x, base=2):
    return int(x, base)


print(int2('1000'))

# 使用偏函数创建 新函数 int2
# 使用 functools.partial 创建偏函数
int2 = functools.partial(int, base=2)

print(int2("111111111111111111"))

# funtools.patial 的作用就是把一个函数的某些参数给固定住，也就是
# 设置默认值，返回一个新的函数，使用这个新的函数会更简单
