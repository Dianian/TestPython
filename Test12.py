# 
# Created by 付博文 on 2017/9/30.
# 

# 切片

L = ['Admin', 'Jack', 'Bob', '45161425', '541646']

print(L[0:3])  # 切片操作 取前三个元素
# 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素

# 如果第一个元素是0，可以省略
print(L[:3])

# 取到数第一个元素
print(L[-1])
# 倒数切片
print(L[-2:-1])

L = list(range(100))
# 前十个 每隔两个取一个
print(L[:10:2])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串