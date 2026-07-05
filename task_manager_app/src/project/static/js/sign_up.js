    const passwordInput = document.getElementById("password");
    const showPassword = document.getElementById("show-password");

    showPassword.addEventListener("change", function () {
        passwordInput.type = this.checked ? "text" : "password";
    });

document.getElementById("sign-up-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const firstName = document.getElementById("first-name").value;
    const lastName = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/sign-up", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password
        })
    });

    const result = await response.json();

    if (result.success) {
        alert("Account created successfully.");
        window.location.href = "login.html";
    } else {
        alert("Something went wrong.");
    }
});