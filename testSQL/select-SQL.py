# 
# Created by 付博文 on 2017/10/10.
#

# 查询数据

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句
cursor.execute('select * from user where id=?', ('1',))

# 获得查询结果
value = cursor.fetchall()
print(value)

cursor.close()

conn.close()
