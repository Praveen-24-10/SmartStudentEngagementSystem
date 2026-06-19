import cv2
import os

student_id = input("Enter Student ID: ")

dataset_path = os.path.join(
    "dataset",
    student_id
)

os.makedirs(
    dataset_path,
    exist_ok=True
)

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

count = 0

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

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        count += 1

        filename = os.path.join(
            dataset_path,
            f"{count}.jpg"
        )

        cv2.imwrite(
            filename,
            face
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

    cv2.putText(
        frame,
        f"Images: {count}/50",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Capture Faces",
        frame
    )

    if count >= 50:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Face Dataset Created Successfully")