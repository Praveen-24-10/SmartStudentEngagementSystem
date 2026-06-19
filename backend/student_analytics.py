from flask import Flask, jsonify
from flask_cors import CORS
from db_connection import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/student-analytics/<int:student_id>")
def student_analytics(student_id):

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT STUDENT_ID,
                   NAME,
                   EMAIL
            FROM STUDENTS
            WHERE STUDENT_ID = :id
        """, [student_id])

        student = cursor.fetchone()

        if not student:
            return jsonify({
                "error": "Student not found"
            })

        cursor.execute("""
            SELECT COUNT(*)
            FROM ATTENDANCE
            WHERE STUDENT_ID = :id
        """, [student_id])

        attended = cursor.fetchone()[0]

        total_classes = 40

        missed = total_classes - attended

        attendance_percentage = round(
            (attended / total_classes) * 100,
            2
        )

        return jsonify({
            "student_id": student[0],
            "name": student[1],
            "email": student[2],
            "attended": attended,
            "missed": missed,
            "attendance_percentage":
                attendance_percentage
        })

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