# 返回函数

# 高阶函数除了可以接收函数作为参数 ，还可以把函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 这个例子中 在函数 lazy_sum 中定义了一个 sum ，内部函数可以
# 引用外部函数 lazy_sum  的参数和局部变量 当 lazy_sum 返回函数
# sum 时 ，相关的参数和变量都保存在返回的函数中， 这种程序的结构称为
# 闭包（Closure）

# 当调用 lazy_sum() 时 每次都会返回一个新的函数 即使传入相同的参数

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

print(f1 == f2)  # Flase

# f1() 和 f2() 的调用结果互不影响

