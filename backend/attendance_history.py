from flask import Flask, jsonify
from flask_cors import CORS
from db_connection import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/attendance-history")
def attendance_history():

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                A.ATTENDANCE_ID,
                S.STUDENT_ID,
                S.NAME,
                A.ATTENDANCE_DATE,
                A.STATUS
            FROM ATTENDANCE A
            JOIN STUDENTS S
            ON A.STUDENT_ID = S.STUDENT_ID
            ORDER BY A.ATTENDANCE_DATE DESC
        """)

        rows = cursor.fetchall()

        data = []

        for row in rows:
            data.append({
                "attendance_id": row[0],
                "student_id": row[1],
                "name": row[2],
                "date": str(row[3]),
                "status": row[4]
            })

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass

if __name__ == "__main__":
    app.run(debug=True)