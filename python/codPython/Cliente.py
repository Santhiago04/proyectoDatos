import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'PROYECTO'
    )
    
    print("\n-------------------------------------------TABLA CLIENTE-------------------------------------------")
    cursor = connection.cursor()
    cursor.execute("select * from cliente")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
    
finally:
    connection.close()