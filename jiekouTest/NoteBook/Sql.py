import pymysql

connection = pymysql.connect(host = '10.32.189.250',
                             port = 3306,
                             user = 'clm',
                             password = 'clm',
                             db = 'clm'
                             # charset = 'UTF-8'
                             # cursorclas = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

sql = "SELECT * from t_attendance_record   LIMIT 10 ;"
result = cursor.execute(sql)
print(result)

data = cursor.fetchone()
data1 = cursor.fetchall()
print(data)
print("------------")
for i in data1:
    print(i)

cursor.close()