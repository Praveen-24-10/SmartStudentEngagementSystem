from db_connection import get_connection

def delete_student(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM STUDENTS
        WHERE STUDENT_ID = :1
    """, [student_id])

    connection.commit()

    print("Student deleted successfully.")

    cursor.close()
    connection.close()


student_id = int(input("Enter Student ID to delete: "))

delete_student(student_id)