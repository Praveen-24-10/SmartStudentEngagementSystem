from flask import Flask, jsonify
from flask_cors import CORS

from db_connection import get_connection

app = Flask(__name__)
CORS(app)


@app.route("/dashboard-data")
def dashboard_data():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        # Total Students
        cursor.execute(
            "SELECT COUNT(*) FROM STUDENTS"
        )
        total_students = cursor.fetchone()[0]

        # Total Attendance Records
        cursor.execute(
            "SELECT COUNT(*) FROM ATTENDANCE"
        )
        attendance_records = cursor.fetchone()[0]

        # Present Today
        cursor.execute("""
            SELECT COUNT(DISTINCT STUDENT_ID)
            FROM ATTENDANCE
            WHERE TRUNC(ATTENDANCE_DATE) =
                  TRUNC(SYSDATE)
        """)
        present_today = cursor.fetchone()[0]

        # Absent Today
        absent_today = total_students - present_today

        # Attendance Percentage
        if total_students > 0:
            attendance_percentage = round(
                (present_today / total_students) * 100,
                2
            )
        else:
            attendance_percentage = 0

        data = {
            # Existing Metrics
            "total_students": total_students,
            "attendance_records": attendance_records,
            "engagement_records": 0,
            "attentive_count": 0,
            "distracted_count": 0,
            "today_status": (
                "Present"
                if present_today > 0
                else "No Attendance"
            ),

            # Existing Percentage
            "attendance_rate": attendance_percentage,

            # New Phase-1 Metrics
            "present_today": present_today,
            "absent_today": absent_today,
            "attendance_percentage": attendance_percentage
        }

        return jsonify(data)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    app.run(debug=True)