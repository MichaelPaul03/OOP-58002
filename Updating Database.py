import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\micha\Documents\Database3.accdb;')
    print("Database is connected")

    Fullname = "Michael Paul Meneses"
    user_id = 6

    Address = "Valenzuela"
    user_id = 6

    Contact = 587
    user_id = 6

    record = connection.cursor()
    record.execute('update Table1 SET Fullname=? WHERE id=?',(Fullname,user_id))
    record.execute('update Table1 SET Address=? WHERE id=?', (Address, user_id))
    record.execute('update Table1 SET Contact=? WHERE id=?', (Contact, user_id))
    record.commit()
    print("Database is updated")


except pyodbc.Error as e:
    print("Error in Connection")

