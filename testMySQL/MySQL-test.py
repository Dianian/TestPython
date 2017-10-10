# 
# Created by 付博文 on 2017/10/10.
#

# 导入 MySQL驱动
import mysql.connector

# 连接MySQL数据库
conn = mysql.connector.connect(user='root', password='123456', database='test')

# 创建 coursor
coursor = conn.cursor()

# 执行 SQL 语句 创建user表
coursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录， MySql的占位符是%
# coursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

# 获得插入行数
print(coursor.rowcount)

# 提交事务 执行INSERT等操作后要调用commit()提交事务
conn.commit()
coursor.close()

# 查询
# coursor = conn.cursor()
# coursor.execute('select * from user where id = %s', ('1',))
#
# value = coursor.fetchall()
# print(value)
#
# coursor.close()
# conn.close()
