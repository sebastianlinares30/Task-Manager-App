document.addEventListener("DOMContentLoaded", function () {

    const logoutBtn = document.getElementById("logout-btn");

    logoutBtn.addEventListener("click", async function () {

        await fetch("http://127.0.0.1:5000/logout", {
            method: "POST"
        });

        // Return to the login page.
        window.location.href = "login.html";
    });

});