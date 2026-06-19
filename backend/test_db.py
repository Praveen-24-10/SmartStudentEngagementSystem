from db_connection import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
    SELECT USER
    FROM DUAL
""")

print(
    "Connected User:",
    cursor.fetchone()
)

cursor.execute("""
    SELECT table_name
    FROM user_tables
""")

tables = cursor.fetchall()

print(
    "Number of tables:",
    len(tables)
)

for table in tables:

    print(table)

cursor.close()
connection.close()