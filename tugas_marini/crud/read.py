
import mysql.connector

def read():
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="toko_motor"
    )

    mycursor = mysb.cursor(buffered=True)

    sql = "SELECT * FROM pelanggan"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mycursor.close()
    mysb.close()

    # print(myresult)
    
    for value in myresult:
        print(value)
