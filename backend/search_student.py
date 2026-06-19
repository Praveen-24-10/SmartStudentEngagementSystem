from db_connection import get_connection

student_id = int(input("Enter Student ID: "))

connection = get_connection()
cursor = connection.cursor()

cursor.execute(
    """
    SELECT *
    FROM STUDENTS
    WHERE STUDENT_ID = :1
    """,
    [student_id]
)

row = cursor.fetchone()

if row:
    print(row)
else:
    print("Student Not Found")

cursor.close()
connection.close()