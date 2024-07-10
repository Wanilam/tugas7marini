import mysql.connector

def create_record(id, nama, alamat):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="toko_motor"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO pelanggan (id, nama, alamat) VALUES ( %s, %s, %s)"
    val = (id, nama, alamat)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()