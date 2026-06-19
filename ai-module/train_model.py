import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []

for student_id in os.listdir(dataset_path):

    student_folder = os.path.join(
        dataset_path,
        student_id
    )

    if not os.path.isdir(student_folder):
        continue

    for image_name in os.listdir(student_folder):

        image_path = os.path.join(
            student_folder,
            image_name
        )

        image = cv2.imread(
            image_path,
            cv2.IMREAD_GRAYSCALE
        )

        if image is None:
            continue

        faces.append(image)
        labels.append(int(student_id))

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(
    faces,
    np.array(labels)
)

recognizer.save("trainer.yml")

print("--------------------------------")
print("Model Trained Successfully")
print("Model Saved As trainer.yml")
print("--------------------------------")