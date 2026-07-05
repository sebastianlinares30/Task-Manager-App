// document.getElementById gets the <form id="add-task-form"> from add-task.html and is now 'watching' this form
// .addEventListener("submit", async function (e) { runs when task form is submitted on the add-task.html file
// e.preventDefault(); prevents page from reloading after submit button is selected
document.getElementById("add-task-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const taskName = document.getElementById("task-name").value; // Reads <input id="task-name"> from add-task.html
    const rawDate = document.getElementById("due-date").value; // Reads <input type="date" id="due-date"> from add-task.html
    const userId = localStorage.getItem("user_id"); // Pulls login data from localStorage

    // Converts YYYY-MM-DD to MM/DD/YYYY
    const [year, month, day] = rawDate.split("-");
    const formattedDate = `${month}/${day}/${year}`;

    // await means it'll wait until the server responds
    await fetch("http://127.0.0.1:5000/add-task", {  // Calls @app.route("/add-task", methods=["POST"]) from app.py
        method: "POST", // POST method means it'll create new data not just request data
        headers: {"Content-Type": "application/json"}, // Tells the server/db the payload is in JSON
        body: JSON.stringify({
            user_id: userId,
            task_name: taskName,
            due_date: formattedDate
        })
    });
    window.location.href = "dashboard.html"; // Redirects you back to homepage after task is entered
});