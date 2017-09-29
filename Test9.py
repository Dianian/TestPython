#
# Created by 付博文 on 2017/9/29.
#

# 定义函数
import math


# 定义一个函数要使用def 语句 依次写出函数名、括号、括号中的参数和冒号
# 然后在缩进块中编写函数体，函数的返回值同return语句返回

# 定义一个求绝对值的 my_abs 函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


# 空函数
# 定义一个什么都不做的空函数 可以用pass语句

def nop():
    pass


# pass 也可以用在其他语句里

if 0 > 18:
    pass


# 缺少了 pass 代码运行就会有语法错误

# 修改my_abs的定义 ，对参数类型做检查

def my_abs2(x):
    if not isinstance(x, (int, float)):  # 数据类型检查 内置函数isinstance()
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs2(12))


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# Python 返回的仍是但一值
r = move(100, 100, 60, math.pi / 6)
print(r)

#返回值是一个tuple 但是 返回一个tuple可以省略括号，而多个变量可以同时
#接收一个 tuple 按位置赋给对应的值
