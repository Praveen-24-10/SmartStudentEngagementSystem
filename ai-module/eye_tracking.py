import cv2
import os
import sys

# Backend path
backend_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "backend"
    )
)

sys.path.append(backend_path)

from engagement_service import log_engagement

# Webcam
cap = cv2.VideoCapture(0)

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Eye detector
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

# Temporary student ID
student_id =  1

# Status tracking
previous_status = None

attentive_frames = 0
distracted_frames = 0

# Number of consecutive frames required
FRAME_THRESHOLD = 90

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
        minNeighbors=5
    )

    eyes_detected = False

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray
        )

        if len(eyes) >= 2:
            eyes_detected = True

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

    # Frame counting logic
    if eyes_detected:

        attentive_frames += 1
        distracted_frames = 0

    else:

        distracted_frames += 1
        attentive_frames = 0

    # ATTENTIVE
    if attentive_frames >= FRAME_THRESHOLD:

        if previous_status != "ATTENTIVE":

            previous_status = "ATTENTIVE"

            log_engagement(
                student_id,
                "ATTENTIVE"
            )

            print(
                "Status Changed: ATTENTIVE"
            )

    # DISTRACTED
    elif distracted_frames >= FRAME_THRESHOLD:

        if previous_status != "DISTRACTED":

            previous_status = "DISTRACTED"

            log_engagement(
                student_id,
                "DISTRACTED"
            )

            print(
                "Status Changed: DISTRACTED"
            )

    # Display
    display_status = (
        previous_status
        if previous_status
        else "DETECTING"
    )

    cv2.putText(
        frame,
        display_status,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Smart Student Engagement Monitor",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()