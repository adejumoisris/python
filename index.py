import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "acer"
)


newDatabase = mydb.cursor()


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Tunde", "Shitta")
newDatabase.execute(sql, val)

mydb.commit()

print(newDatabase.rowcount, "Information inserted.")


