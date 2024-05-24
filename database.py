import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host='localhost',       # MySQL host (e.g., localhost)
    user='root',   # MySQL username
    password='abhay@260304',   # MySQL password
    database='loginpage'    # Name of the database you want to connect to
)


cursor = conn.cursor()


sql_formula= " INSERT INTO loginpage(email,password) VALUES(%s,%s)"
user=('abhay@gmail.com','abhay@123')
cursor.execute(sql_formula,user)


conn.commit()


cursor.close()
conn.close()

 