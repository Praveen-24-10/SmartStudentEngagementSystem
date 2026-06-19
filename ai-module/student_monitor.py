import cv2
import sys
import os

# -----------------------------------
# Backend Imports
# -----------------------------------
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
from engagement_service import log_engagement

# -----------------------------------
# Load Face Recognition Model
# -----------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()

model_path = os.path.join(
    os.path.dirname(__file__),
    "trainer.yml"
)

recognizer.read(model_path)

# -----------------------------------
# Face Detector
# -----------------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# -----------------------------------
# Eye Detector
# -----------------------------------
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

# -----------------------------------
# Webcam
# -----------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Cannot access webcam")
    exit()

# -----------------------------------
# Variables
# -----------------------------------
attendance_marked = False

recognized_student_id = None

student_name = "Unknown"

current_status = "DETECTING"

last_logged_status = None

attentive_frames = 0

distracted_frames = 0

FRAME_THRESHOLD = 60

# -----------------------------------
# Main Loop
# -----------------------------------
while True:

    ret, frame = cap.read()

    if not ret:
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

        try:

            student_id, confidence = (
                recognizer.predict(face_roi)
            )

        except Exception:
            continue

        if confidence < 80:

            recognized_student_id = student_id

            try:

                student_name = get_student_name(
                    student_id
                )

            except Exception:

                student_name = "Unknown"

            # -----------------------------------
            # Attendance
            # -----------------------------------
            if not attendance_marked:

                try:

                    success = mark_attendance(
                        student_id
                    )

                    if success:

                        attendance_marked = True

                        print(
                            f"Attendance Marked "
                            f"for {student_name}"
                        )

                except Exception as e:

                    print(
                        "Attendance Error:",
                        e
                    )

            # -----------------------------------
            # Eye Detection
            # -----------------------------------
            eyes = eye_cascade.detectMultiScale(
                face_roi
            )

            for (ex, ey, ew, eh) in eyes:

                cv2.rectangle(
                    frame,
                    (x + ex, y + ey),
                    (x + ex + ew,
                     y + ey + eh),
                    (0, 255, 0),
                    2
                )

            # -----------------------------------
            # Frame Counting Logic
            # -----------------------------------
            if len(eyes) >= 1:

                attentive_frames += 1
                distracted_frames = 0

            else:

                distracted_frames += 1
                attentive_frames = 0

            # -----------------------------------
            # ATTENTIVE
            # -----------------------------------
            if attentive_frames >= FRAME_THRESHOLD:

                current_status = "ATTENTIVE"

                if (
                    last_logged_status
                    != "ATTENTIVE"
                ):

                    try:

                        log_engagement(
                            student_id,
                            "ATTENTIVE"
                        )

                        print(
                            f"{student_name}: "
                            f"ATTENTIVE"
                        )

                    except Exception as e:

                        print(
                            "Engagement Error:",
                            e
                        )

                    last_logged_status = (
                        "ATTENTIVE"
                    )

            # -----------------------------------
            # DISTRACTED
            # -----------------------------------
            elif distracted_frames >= FRAME_THRESHOLD:

                current_status = "DISTRACTED"

                if (
                    last_logged_status
                    != "DISTRACTED"
                ):

                    try:

                        log_engagement(
                            student_id,
                            "DISTRACTED"
                        )

                        print(
                            f"{student_name}: "
                            f"DISTRACTED"
                        )

                    except Exception as e:

                        print(
                            "Engagement Error:",
                            e
                        )

                    last_logged_status = (
                        "DISTRACTED"
                    )

            label = (
                f"{student_name} "
                f"(ID:{student_id})"
            )

        else:

            label = "Unknown Face"

        # -----------------------------------
        # Draw Face Rectangle
        # -----------------------------------
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
            0.7,
            (0, 255, 0),
            2
        )

    # -----------------------------------
    # Dashboard Text
    # -----------------------------------
    if attendance_marked:

        attendance_text = (
            f"Attendance Marked - "
            f"{student_name}"
        )

    else:

        attendance_text = (
            "Waiting For Face..."
        )

    cv2.putText(
        frame,
        attendance_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Status: {current_status}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.imshow(
        "Smart Student Engagement Monitor",
        frame
    )

    key = cv2.waitKey(1)

    if key & 0xFF == 27:
        break

# -----------------------------------
# Cleanup
# -----------------------------------
cap.release()

cv2.destroyAllWindows()