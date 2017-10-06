# 生成器

# generator

# 创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了

# 把列表生成式的 [] 替换成 （）就创建了一个 geneator

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
# print(g)

# L 和 g 的区别 L是一个 list , g是 一个 generater

# 如果要打印 generater 通过 next 函数获得下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 使用 for 循环迭代

g = (x * x for x in range(10))
for n in g:
    print(n)
