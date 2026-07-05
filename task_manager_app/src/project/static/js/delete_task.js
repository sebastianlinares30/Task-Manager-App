document.addEventListener("DOMContentLoaded", function () {
    const deleteModeBtn = document.getElementById("delete-mode-btn");

    deleteModeBtn.addEventListener("click", function () {
        const checkboxes = document.querySelectorAll(".task-checkbox");

        checkboxes.forEach(checkbox => {
            checkbox.style.display = "inline-block";
        });

        deleteModeBtn.textContent = "Confirm Delete";

        deleteModeBtn.onclick = async function () {
            const selected = document.querySelectorAll(".task-checkbox:checked");

            if (selected.length === 0) {
                alert("Please select at least one task.");
                return;
            }

            const confirmDelete = confirm("Are you sure you want to delete the selected task(s)?");

            if (!confirmDelete) {
                return;
            }

            for (const checkbox of selected) {
                const taskId = checkbox.dataset.taskId;

                await fetch("http://127.0.0.1:5000/delete-task", {
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        task_id: taskId
                    })
                });
            }

            alert("Task deleted successfully.");
            location.reload();
        };
    });
});