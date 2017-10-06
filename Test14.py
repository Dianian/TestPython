# 
# Created by 付博文 on 2017/9/30.
#

# 列表生成式
# range()

# 生成 1 - 10 整数
print(list(range(1, 11)))

# 生成[1x1,2x2,3x3,4x4……10x10]
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 或者
print([x * x for x in range(1, 11)])

# 写列表生成式， 把要生成的元素 x*x 放在前面 后面跟for循环
# 就可以把 list 创建出来

# for 后面加上 if 判断 可以筛选出偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 使用两层循环 可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
