document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("login-btn");

    btn.addEventListener("click", async function () {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const result = await response.json();

        if (result.success) {
            window.location.href = "home.html";
        } else {
            alert("Invalid login");
        }
    });

});