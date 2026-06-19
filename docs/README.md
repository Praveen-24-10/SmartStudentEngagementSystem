
# 🎓 Smart Student Engagement Monitoring System

## 📖 About the Project

The **Smart Student Engagement Monitoring System** is a web-based application developed to manage student information, track attendance records, and provide attendance analytics through an interactive dashboard.

The system integrates a modern frontend, Flask backend services, Oracle Database storage, and OpenCV-based AI modules to create a centralized student monitoring platform.

This project was developed as an academic project at **VIT-AP University** to demonstrate database integration, web application development, attendance management, and AI-based monitoring concepts.

---

# 🎯 Project Objectives

The objectives of this project are:

* Maintain student records digitally.
* Automate attendance management.
* Store attendance information securely.
* Provide attendance analytics through dashboards.
* Integrate AI-based face detection capabilities.
* Reduce manual record management.
* Improve classroom monitoring and reporting.

---

# 🏗 System Architecture

```text
Student/User
      │
      ▼
Frontend (HTML, CSS, JavaScript)
      │
      ▼
Flask Backend APIs
      │
      ▼
Oracle Database 21c XE
      │
      ▼
Dashboard & Analytics

AI Module (OpenCV)
      │
      ▼
Face Detection & Monitoring
```

---

# 🚀 Complete Workflow

## Step 1: Student Registration

The first step is registering students in the system.

### Information Collected

* Student Name
* Student Email

### Registration Process

1. Open the Student Registration page.
2. Enter the student's name.
3. Enter the student's email address.
4. Click the Register button.
5. The data is sent to the Flask backend.
6. The backend stores the student information in the Oracle Database.

### Example

```text
Student ID : 1
Name       : John Doe
Email      : john@gmail.com
```

---

## Step 2: Face Registration

After student registration, face images can be collected for AI processing.

### Process

1. Open the webcam.
2. Capture multiple face images.
3. Save face images into the dataset directory.
4. Associate images with a Student ID.
5. Train the OpenCV model.

### Files Used

```text
capture_faces.py
train_model.py
trainer.yml
```

### Purpose

Creates a dataset for future face recognition and attendance automation.

---

## Step 3: Face Detection Module

The system contains an OpenCV-based face detection module.

### Process

1. Start the webcam.
2. Detect faces using Haar Cascade Classifiers.
3. Draw bounding boxes around detected faces.
4. Display detected faces in real time.

### File Used

```text
face_detection.py
```

### Output

```text
Face Detected Successfully
```

---

## Step 4: Attendance Management

Attendance records are maintained in the database.

### Process

1. Student attendance is recorded.
2. Attendance data is stored in Oracle Database.
3. Attendance history is maintained.
4. Attendance statistics are generated.

### Attendance Table Example

```text
Attendance ID : 1
Student ID    : 1
Date          : 18-JUN-2026
Status        : Present
```

---

## Step 5: Student Search

The system provides a student search module.

### Process

1. Enter Student ID.
2. Click Search.
3. Student details are retrieved from the database.
4. Attendance statistics are calculated.
5. Results are displayed.

### Information Displayed

* Student ID
* Student Name
* Student Email
* Classes Attended
* Classes Missed
* Attendance Percentage

---

## Step 6: Attendance History

The attendance history module displays all attendance records.

### Features

* Attendance ID
* Student Name
* Attendance Date
* Attendance Status

### Process

1. Query attendance records.
2. Retrieve data from Oracle Database.
3. Display records in tabular format.

---

## Step 7: Dashboard Analytics

The dashboard provides real-time statistics.

### Dashboard Features

* Total Students
* Attendance Records
* Present Students
* Absent Students
* Attendance Percentage
* Attendance Overview Chart

### Dashboard Workflow

```text
Oracle Database
        │
        ▼
Flask API
        │
        ▼
Dashboard Page
        │
        ▼
Analytics & Charts
```

---

# 🗄 Database Design

## STUDENTS Table

| Column Name | Data Type     |
| ----------- | ------------- |
| STUDENT_ID  | NUMBER        |
| NAME        | VARCHAR2(100) |
| EMAIL       | VARCHAR2(100) |

### Purpose

Stores registered student information.

---

## ATTENDANCE Table

| Column Name     | Data Type    |
| --------------- | ------------ |
| ATTENDANCE_ID   | NUMBER       |
| STUDENT_ID      | NUMBER       |
| ATTENDANCE_DATE | DATE         |
| STATUS          | VARCHAR2(20) |

### Purpose

Stores attendance records of students.

---

# 🔌 Oracle Database Connection

Database communication is handled through Python.

### Connection Flow

```text
Frontend
   │
   ▼
Flask Backend
   │
   ▼
db_connection.py
   │
   ▼
Oracle Database (XEPDB1)
```

### Example Connection

```python
import oracledb

connection = oracledb.connect(
    user="system",
    password="your_password",
    dsn="localhost/XEPDB1"
)
```

### Purpose

Provides access to:

* Student Registration
* Student Search
* Attendance Management
* Dashboard Analytics

---

# 🤖 AI Module

The project contains an AI module developed using OpenCV.

### Components

#### capture_faces.py

Captures face samples for training.

#### train_model.py

Trains the face dataset.

#### face_detection.py

Detects faces using webcam input.

#### eye_tracking.py

Tracks eye movement.

#### student_monitor.py

Monitors student engagement activities.

### Future Scope

* Face Recognition Attendance
* Eye Attention Detection
* Student Engagement Scoring
* Automated Attendance Recording

---

# 🛠 Technologies Used

| Technology             | Purpose               |
| ---------------------- | --------------------- |
| Python                 | Backend Development   |
| Flask                  | REST API Development  |
| OpenCV                 | Face Detection        |
| Oracle Database 21c XE | Database              |
| HTML5                  | Frontend Development  |
| CSS3                   | User Interface Design |
| JavaScript             | Client-side Logic     |
| Chart.js               | Dashboard Charts      |

---

# 📂 Project Structure

```text
SmartStudentEngagementSystem/

├── ai-module/
│   ├── capture_faces.py
│   ├── face_detection.py
│   ├── eye_tracking.py
│   ├── student_monitor.py
│   ├── train_model.py
│   └── trainer.yml
│
├── backend/
│   ├── db_connection.py
│   ├── dashboard_data.py
│   ├── student_analytics.py
│   └── other_api_files
│
├── database/
│   └── schema.sql
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── dashboard.html
│   ├── students.html
│   ├── searchstudent.html
│   ├── attendance.html
│   └── attendance_history.html
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1. Install Oracle Database 21c XE

Create:

* STUDENTS table
* ATTENDANCE table

---

## 2. Install Required Python Packages

```bash
pip install flask
pip install flask-cors
pip install opencv-python
pip install numpy
pip install oracledb
```

---

## 3. Configure Database Connection

Update database credentials in:

```text
backend/db_connection.py
```

---

## 4. Run Backend Server

```bash
python dashboard_data.py
```

---

## 5. Launch Frontend

Open:

```text
frontend/dashboard.html
```

using Live Server in Visual Studio Code.

---

# 📸 Screenshots

Add screenshots of:

* Dashboard
* Student Registration
* Student Search
* Attendance History
* Attendance Status

---

# 🎓 Learning Outcomes

Through this project, the following concepts were learned:

* Oracle Database Integration
* Flask API Development
* Frontend Development
* Attendance Management Systems
* Dashboard Analytics
* OpenCV Face Detection
* Database Design
* Client-Server Architecture

---

# 🏫 Institution

VIT-AP University

Amaravati, Andhra Pradesh, India

---

# 👨‍💻 Author

**Tholeti Sri Raj Praveen**

B.Tech Computer Science and Engineering

VIT-AP University

Academic Project – 2026

---

# 📄 License

This project is developed for academic and educational purposes only.
