# 
# Created by 付博文 on 2017/9/30.
#

# 迭代
# 给定一个 list 或 tuple 通过for 循环来遍历这个 list 或 tuple ，这种遍历
# 我们称之为迭代

from collections import Iterable

# dict 迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# dict 的 value 迭代
for value in d.values():
    print(value)

# 同时迭代 key 和 value
for k, v in d.items():
    print(k, v)

# 判断一个对象是否可以迭代

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# 对 list 实现 Java 下标循环
# 内置的 enumerate 可以把 list 变为 索引-元素 对
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
