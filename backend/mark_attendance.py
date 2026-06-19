from db_connection import get_connection
from attendance_service import mark_attendance


def student_exists(student_id):

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM STUDENTS
            WHERE STUDENT_ID = :1
        """, [student_id])

        count = cursor.fetchone()[0]

        return count > 0

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass


def main():

    try:

        print("--------------------------------")
        print("Smart Attendance System")
        print("--------------------------------")

        student_id = int(
            input("Enter Student ID: ")
        )

        if not student_exists(student_id):

            print("--------------------------------")
            print("Student Not Found")
            print("--------------------------------")

            return

        mark_attendance(student_id)

        print("--------------------------------")
        print("Attendance Process Completed")
        print("--------------------------------")

    except ValueError:

        print("--------------------------------")
        print("Please enter a valid Student ID")
        print("--------------------------------")

    except Exception as e:

        print("--------------------------------")
        print("Database Error:")
        print(e)
        print("--------------------------------")


if __name__ == "__main__":
    main()