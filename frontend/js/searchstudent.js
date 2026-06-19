document.addEventListener(
    "DOMContentLoaded",
    () => {

        document.getElementById(
            "searchBtn"
        ).addEventListener(
            "click",
            async () => {

                const studentId =
                    document.getElementById(
                        "studentId"
                    ).value;

                if (!studentId) {
                    alert(
                        "Please enter a Student ID"
                    );
                    return;
                }

                try {

                    const response =
                        await fetch(
                            `http://127.0.0.1:5000/student-analytics/${studentId}`
                        );

                    const data =
                        await response.json();

                    if (data.error) {

                        alert(
                            data.error
                        );

                        return;
                    }

                    document.getElementById(
                        "studentIdResult"
                    ).innerText =
                        data.student_id;

                    document.getElementById(
                        "studentNameResult"
                    ).innerText =
                        data.name;

                    document.getElementById(
                        "emailResult"
                    ).innerText =
                        data.email;

                    document.getElementById(
                        "attendedResult"
                    ).innerText =
                        data.attended;

                    document.getElementById(
                        "missedResult"
                    ).innerText =
                        data.missed;

                    document.getElementById(
                        "attendancePercentageResult"
                    ).innerText =
                        data.attendance_percentage + "%";

                } catch (error) {

                    console.error(
                        "Search Error:",
                        error
                    );

                    alert(
                        "Unable to connect to server."
                    );
                }

            }
        );

    }
);