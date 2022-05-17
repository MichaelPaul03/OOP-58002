import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\micha\Documents\Database3.accdb;')
    print("Database is connected")

    user_id = 6
    record = connect.cursor()
    record.execute('DELETE from Table1 WHERE id = ?',(user_id))
    record.commit()
    print("Data is deleted")


except pyodbc.Error as e:
    print("Error in Connection")