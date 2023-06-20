document.addEventListener("DOMContentLoaded", function() {
    var passwordInput = document.getElementById("password1");
    var secpasswordInput = document.getElementById("password2");
    var errorMessage = document.getElementById("error-message");
    var errorMessage2 = document.getElementById("error-message2");
    var form = document.getElementById("my-form");

    passwordInput.addEventListener("input", function() {
        var password = passwordInput.value;
        var passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,}$/;

        if (!password) {
            errorMessage.textContent = "Please enter a password.";
            form.classList.add("disable-submit");
        } else if (!passwordPattern.test(password)) {
            errorMessage.textContent = "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.";
            form.classList.add("disable-submit");
        } else {
            errorMessage.textContent = "";
            form.classList.remove("disable-submit");
        }
    });

    secpasswordInput.addEventListener('input', function() {
        var password1 = passwordInput.value;
        var password = secpasswordInput.value;
        
        if (!password) {
            errorMessage2.textContent = "Please enter a password.";
            form.classList.add("disable-submit");
        } else if (password1 !== password) {
            errorMessage2.textContent = "Passwords must match!";
            form.classList.add("disable-submit");
        } else {
            errorMessage2.textContent = "";
            form.classList.remove("disable-submit");
        }
    });
});
