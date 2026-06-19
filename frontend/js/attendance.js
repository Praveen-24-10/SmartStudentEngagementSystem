document.addEventListener("DOMContentLoaded", loadAttendance);

async function loadAttendance() {
    try {
        const response = await fetch(
            "http://127.0.0.1:5000/attendance-history"
        );

        const data = await response.json();

        const tableBody =
            document.querySelector(
                "#attendanceTable tbody"
            );

        tableBody.innerHTML = "";

        data.forEach(record => {

            const row =
                document.createElement("tr");

            row.innerHTML = `
                <td>${record.attendance_id}</td>
                <td>${record.name}</td>
                <td>${record.date}</td>
                <td>${record.status}</td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {

        console.error(
            "Error loading attendance:",
            error
        );
    }
}