import pyodbc

# Define your connection parameters
server = 'funcappdemoserver.database.windows.net'
database = 'funcappdemo'
username = 'adminrevathi'
password = 'Rev@thi2592'
driver = '{ODBC Driver 18 for SQL Server}'  # Or 18 if installed

print("inside insertsqlfile")
# Create connection string
connection_string = f'''
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''

# Connect to Azure SQL Database
try:
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        
        # Insert 2 sample rows
        insert_query = "INSERT INTO demoTable (id, name) VALUES (?, ?)"
        sample_data = [(3, 'Tom'), (4, 'Harry')]

        cursor.executemany(insert_query, sample_data)
        conn.commit()
        print("Rows inserted successfully.")

except Exception as e:
    print("Error:", e)

