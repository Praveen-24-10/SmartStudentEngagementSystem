from db_connection import get_connection


def add_student(name, email):

    if not name.strip():
        print("Name cannot be empty")
        return False

    if "@" not in email:
        print("Invalid email")
        return False

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO STUDENTS
            (
                NAME,
                EMAIL
            )
            VALUES
            (
                :1,
                :2
            )
            """,
            [name, email]
        )

        connection.commit()

        print("Student Registered Successfully")

        return True

    except Exception as e:

        print("Database Error:")
        print(e)

        return False

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass


def get_student_name(student_id):

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT NAME
            FROM STUDENTS
            WHERE STUDENT_ID = :1
            """,
            [student_id]
        )

        row = cursor.fetchone()

        if row:
            return row[0]

        return "Unknown"

    except Exception:

        return "Unknown"

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass