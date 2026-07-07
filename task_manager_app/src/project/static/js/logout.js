document.addEventListener("DOMContentLoaded", function () {

    const logoutBtn = document.getElementById("logout-btn");

    logoutBtn.addEventListener("click", function () {

        // Remove the current user's session.
        localStorage.removeItem("user_id");

        // Return to the login page.
        window.location.href = "login.html";
    });

});