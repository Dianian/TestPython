# 
# Created by 付博文 on 2017/10/10.
# 

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')

# 创建一个 Cursor
cursor = conn.cursor()

# 执行一条 SQL 语句 ，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 继续执行 SQL 语句 ，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# 通过 rowcount 获得插入行数
print(cursor.rowcount)

# 关闭 Cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭Connection
conn.close()


#查询记录
conn=sqlite3.connect("test.db")
cursor=conn.cursor()

