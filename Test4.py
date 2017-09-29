#
# Created by 付博文 on 2017/9/29.
#

# list 和 tuple


# list列表 有序的集合

list = ["asd", 'Bob', 'fgg']
print(list)

# len() 函数可以获得list的个数
print(len(list))

# 用引索来访问每一个元素的位置
print(list[0])
print(list[2])

# 当索引超出了范围时，Python会报一个IndexError错误
# ，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1

# 直接取最后一个元素
print(list[-1])

# 倒数第二个
print(list[-2])

#使用 append() 追加元素到末尾
list.append('Admin')
print(list)

#使用 insert() 插入元素到指定位置
list.insert(1,'Jack')
print(list)

# 删除末尾的元素用 pop() 方法
list.pop()
print(list)

# 删除指定位置的元素 pop(i)
list.pop(1)
print(list)

# 把某个元素替换成别的元素
list[1]='aaaaaaaaa'
print(list)

# list 里面的元素可以是不同的元素
L=['abc',True,100]
print(len(L))
print(L)

# list的元素也可以是另一个list
s=['python','java',['asp','php'],'c#']
print(len(s))
print(s)

# tuple 一种有序列表 叫元组 tuple和list非常相似 但是tuple一旦被初始化就不能修改了
tuple=("Michael",'Bob','Jack')
print(len(tuple))
print(tuple)

#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t=(1,2)
print(t)

# 定义一个空的tuple
t=()
print(t)

#定义一个元素的touple
t=(1,)
#不能 t=(1)
#这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
# 这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
print(t)

#可变的touple
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)