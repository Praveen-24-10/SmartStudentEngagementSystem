from db_connection import get_connection

def update_student(student_id, name, email):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE STUDENTS
        SET NAME = :1,
            EMAIL = :2
        WHERE STUDENT_ID = :3
    """, [name, email, student_id])

    connection.commit()

    print("Student updated successfully.")

    cursor.close()
    connection.close()


student_id = int(input("Enter Student ID: "))
name = input("Enter New Name: ")
email = input("Enter New Email: ")

update_student(student_id, name, email)