import pyodbc
server = 'spaceturtle.database.windows.net'
database = 'spaceturtle'
username = 'spaceturtle'
password = 'abKhzQip1|-l'
driver= '{ODBC Driver 13 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()