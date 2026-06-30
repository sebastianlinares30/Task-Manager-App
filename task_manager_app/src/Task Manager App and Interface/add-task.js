document.getElementById("add-task-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const taskName = document.getElementById("task-name").value;
    const dueDate = document.getElementById("due-date").value;

    await fetch("/add-task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: taskName,
            due_date: dueDate
        })
    });

    window.location.href = "/view-task";
});