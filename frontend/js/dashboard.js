console.log("dashboard.js loaded");

document.addEventListener(
    "DOMContentLoaded",
    () => {

        console.log("Dashboard started");

        fetch(
            "http://127.0.0.1:5000/dashboard-data"
        )
        .then(response => response.json())
        .then(data => {

            console.log(data);

            document.getElementById(
                "totalStudents"
            ).innerText =
                data.total_students;

            document.getElementById(
                "attendanceRecords"
            ).innerText =
                data.attendance_records;

            document.getElementById(
                "engagementRecords"
            ).innerText =
                data.engagement_records;

            document.getElementById(
                "attentiveCount"
            ).innerText =
                data.attentive_count;

            document.getElementById(
                "distractedCount"
            ).innerText =
                data.distracted_count;

            document.getElementById(
                "attendanceRate"
            ).innerText =
                data.attendance_rate + "%";

            document.getElementById(
                "presentToday"
            ).innerText =
                data.present_today;

            document.getElementById(
                "absentToday"
            ).innerText =
                data.absent_today;

            document.getElementById(
                "todayStatus"
            ).innerText =
                "✅ System Active";

            // Attendance Pie Chart
            const ctx =
                document.getElementById(
                    "attendanceChart"
                );

            new Chart(ctx, {
                type: "pie",

                data: {
                    labels: [
                        "Present",
                        "Absent"
                    ],

                    datasets: [{
                        data: [
                            data.present_today,
                            data.absent_today
                        ]
                    }]
                },

                options: {
                    responsive: true,

                    plugins: {
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            });

        })
        .catch(error => {

            console.error(
                "Dashboard Error:",
                error
            );

            document.getElementById(
                "todayStatus"
            ).innerText =
                "❌ API Offline";
        });

    }
);

// Auto refresh every 10 seconds
setInterval(() => {
    location.reload();
}, 10000);