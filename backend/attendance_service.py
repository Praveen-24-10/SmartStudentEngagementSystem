from db_connection import get_connection


def mark_attendance(student_id):

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM ATTENDANCE
            WHERE STUDENT_ID = :1
            AND TRUNC(ATTENDANCE_DATE) = TRUNC(SYSDATE)
        """, [student_id])

        count = cursor.fetchone()[0]

        if count > 0:

            print("Attendance Already Marked Today")
            return False

        cursor.execute("""
            INSERT INTO ATTENDANCE
            (
                STUDENT_ID,
                ATTENDANCE_DATE,
                STATUS
            )
            VALUES
            (
                :1,
                SYSDATE,
                'PRESENT'
            )
        """, [student_id])

        connection.commit()

        print("Attendance Marked Successfully")

        return True

    except Exception as e:

        print("Attendance Error:")
        print(e)

        return False

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass