document.addEventListener("DOMContentLoaded", async function () { // Waits until webpage is fully loaded/all HTML elements exist

    const container = document.getElementById("display-tasks"); // Reads <div id="display-tasks"> from home.html
    const userId = localStorage.getItem("user_id"); // Pulls login data from localStorage.setItem("user_id", result.user_id); from script.js
    const response = await fetch(`http://127.0.0.1:5000/get-tasks?user_id=${userId}`); // Calls @app.route("/get-tasks") from app.py
    const tasks = await response.json(); // Converts response into JSON

    tasks.forEach(task => { // Runs per task(s)
        const nameParagraph = document.createElement("p"); // Creates <p></p>
        nameParagraph.className = "task-item task-name"; // Inserts into <p></p> and get <p class="task-item task-name"></p>
        nameParagraph.textContent = task.task_name; // Inserts text into <p class="task-item task-name"></p> so we get <p class="task-item task-name">EXAMPLE</p>

        const dateParagraph = document.createElement("p"); // Creates <p></p>
        dateParagraph.className = "task-item due-date"; // Inserts into <p></p> and get <p class="task-item due-date"></p>
        dateParagraph.textContent = task.due_date; // Inserts date into <p></p> and get <p class="task-item due-date">01/01/2026</p>

        container.appendChild(nameParagraph); // Appends it into DOM
        container.appendChild(dateParagraph); // Appends it into DOM
    });
});