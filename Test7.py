#
# Created by 付博文 on 2017/9/29.
#

# dict 和 set


# dite 在其他语言中成为map 使用键-值存储
d = {"Admin": 90, "Bob": 80, 'Jack': 70}
print(d)
print(d['Bob'])

# 除了初始化时指定 还可以通过key放入
d['Bob'] = 1111111111
print(d['Bob'])

# 一个key只能对应一个value 多次对一个key放入value，后面的值会把前面的值冲掉
d['Bob'] = 22222222222222222
print(d['Bob'])

# key不存在 dict就会报错
# 避免key不存在的错误 一种是通过in判断key是否存在
print('Thomas' in d)
# 二是通过dict提供的get方法 如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas'), -1)

# 要删除一个Key用pop(Key) 对应value也会从dict中删除
d.pop("Admin")
print(d)

# dict内部存放的顺序，和key放入的顺序是没有关系的

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
#
# 所以dict是用空间来换取时间的一种方法

# 正确使用Key 非常重要，dict的key必须是不可变对象


# set set和dict类似 也是一组key的集合，但不存储value，所以在set中 没有重复的key

# 创建一个set，需要提供一个list作为输入集合
# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}
# 只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
s = set([1, 2, 3])
print(s)

# 重复的元素在set中自动被过滤
s = set([1, 1, 2, 3, 3, 3, 3])
print(s)

# 通过add()方法可以添加元素到set中，可以重负添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)

# 使用remove(key) 方法可以删除元素
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的
# 交集、并集 等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。


