document.addEventListener("DOMContentLoaded", function () { // Waits until webpage is fully loaded/all HTML elements exist

    const btn = document.getElementById("login-btn"); // Reads <button type="button" id="login-btn">Login</button> from index.html

    btn.addEventListener("click", async function () { // Runs when button is clicked on index.html
        const username = document.getElementById("username").value; // Reads <input type="text" id="username" name="username">
        const password = document.getElementById("password").value; // Reads <input type="text" id="password" name="password">
        const response = await fetch("http://127.0.0.1:5000/login", { // Calls @app.route("/login", methods=["POST"]) from app.py
            method: "POST", // POST method means it'll create new data not just request data
            headers: { // Tells the server/db the payload is in JSON
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const result = await response.json(); // Takes HTTP response from Flask and converts from JSON to JS

        if (result.success) { // Checks if login was valid
            
            window.location.href = "dashboard.html"; // Sends user to dashboard.html if login was successful
        } else {
            alert("Invalid login"); // Alerts if login is invalid
        }
    });

});