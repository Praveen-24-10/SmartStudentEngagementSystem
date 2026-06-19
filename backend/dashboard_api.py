from flask import Flask, jsonify
from flask_cors import CORS

from db_connection import get_connection
from student_service import get_student_name

app = Flask(__name__)

CORS(app)


@app.route("/dashboard-data")
def dashboard_data():

    try:

        connection = get_connection()
        cursor = connection.cursor()

        # Students
        cursor.execute(
            "SELECT COUNT(*) FROM STUDENTS"
        )
        students = cursor.fetchone()[0]

        # Attendance
        cursor.execute(
            "SELECT COUNT(*) FROM ATTENDANCE"
        )
        attendance = cursor.fetchone()[0]

        # Engagement
        cursor.execute(
            "SELECT COUNT(*) FROM ENGAGEMENT_LOG"
        )
        engagement = cursor.fetchone()[0]

        # Attentive
        cursor.execute("""
            SELECT COUNT(*)
            FROM ENGAGEMENT_LOG
            WHERE STATUS = 'ATTENTIVE'
        """)
        attentive = cursor.fetchone()[0]

        # Distracted
        cursor.execute("""
            SELECT COUNT(*)
            FROM ENGAGEMENT_LOG
            WHERE STATUS = 'DISTRACTED'
        """)
        distracted = cursor.fetchone()[0]

        attendance_rate = 0

        if students > 0:

            attendance_rate = round(
                (attendance / students) * 100,
                2
            )

        return jsonify({
            "students": students,
            "attendance": attendance,
            "engagement": engagement,
            "attentive": attentive,
            "distracted": distracted,
            "attendance_rate": attendance_rate
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass


@app.route("/attendance-history")
def attendance_history():

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                A.ATTENDANCE_ID,
                S.NAME,
                A.ATTENDANCE_DATE,
                A.STATUS
            FROM ATTENDANCE A
            JOIN STUDENTS S
            ON A.STUDENT_ID = S.STUDENT_ID
            ORDER BY A.ATTENDANCE_DATE DESC
        """)

        records = []

        for row in cursor.fetchall():

            records.append({
                "attendance_id": row[0],
                "student_name": row[1],
                "date": str(row[2]),
                "status": row[3]
            })

        return jsonify(records)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

    finally:

        try:
            cursor.close()
            connection.close()
        except:
            pass


@app.route("/student/<int:student_id>")
def get_student(student_id):

    try:

        name = get_student_name(student_id)

        return jsonify({
            "student_id": student_id,
            "name": name
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )