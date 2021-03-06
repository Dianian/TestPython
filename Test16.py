# 迭代器

# 凡是可作用于for循环的对象都是Iterable（可迭代对象）类型；
#
# 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。