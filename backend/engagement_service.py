from db_connection import get_connection


def log_engagement(student_id, status):

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO ENGAGEMENT_LOG
            (
                STUDENT_ID,
                STATUS
            )
            VALUES
            (
                :1,
                :2
            )
        """, [student_id, status])

        connection.commit()

        print(
            f"Engagement Logged: "
            f"Student {student_id} - {status}"
        )

    except Exception as e:

        print("Engagement Error:")
        print(e)

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass