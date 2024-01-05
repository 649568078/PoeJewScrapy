import pymysql

# 假设你的数据是一个包含多个值的元组
ids_to_update = (1,)

# 创建 MySQL 数据库连接
connection = pymysql.connect(
    host='10.33.12.96   ',
    user='root',
    password='xx19941130',
    database='poe'
)

cursor = connection.cursor()

# 使用参数化查询
placeholders = ', '.join(['%s'] * len(ids_to_update))
query = f"UPDATE your_table SET bb = %s WHERE id IN ({placeholders})"
new_value = 'new_value'  # 你要设置的新值

# 注意：pymysql 自动将元组参数转换为正确的类型
parameters = (new_value,) + ids_to_update
print(query,parameters)
cursor.execute(query, parameters)

# 提交更改
connection.commit()

# 关闭连接
connection.close()