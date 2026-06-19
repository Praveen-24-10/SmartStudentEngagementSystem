import cv2
import sys
import os

backend_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "backend"
    )
)

sys.path.append(backend_path)

from attendance_service import mark_attendance
from student_service import get_student_name

recognizer = cv2.face.LBPHFaceRecognizer_create()
model_path = os.path.join(
    os.path.dirname(__file__),
    "trainer.yml"
)

recognizer.read(model_path)

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

attendance_marked = False
student_name = ""
recognized_student_id = None

while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        face_roi = gray[
            y:y+h,
            x:x+w
        ]

        student_id, confidence = recognizer.predict(
            face_roi
        )

        if confidence < 80:

            recognized_student_id = student_id

            try:

                student_name = get_student_name(
                    recognized_student_id
                )

            except Exception:
                student_name = "Unknown"

            if not attendance_marked:

                attendance_marked = True

                try:

                    mark_attendance(
                        recognized_student_id
                    )

                    print(
                        f"Attendance Marked for "
                        f"{student_name}"
                    )

                except Exception as e:

                    print(
                        "Database Error:",
                        e
                    )

            label = (
                f"{student_name} "
                f"(ID:{recognized_student_id})"
            )

        else:

            label = "Unknown Face"

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    if attendance_marked:

        status = (
            f"Attendance Marked - "
            f"{student_name}"
        )

    else:

        status = "Waiting for Face"

    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Smart Student Engagement Monitor",
        frame
    )

    key = cv2.waitKey(1)

    if key & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()