function setupPasswordToggle(inputId, buttonId) {

    const input = document.getElementById(inputId);
    const button = document.getElementById(buttonId);

    if (!input || !button) return;

    button.addEventListener("click", function () {

        if (input.type === "password") {

            input.type = "text";

            button.innerHTML =
                '<i class="fa-solid fa-eye-slash"></i>';

        } else {

            input.type = "password";

            button.innerHTML =
                '<i class="fa-solid fa-eye"></i>';

        }

    });

}

setupPasswordToggle("id_password", "togglePassword");

setupPasswordToggle("id_password1", "togglePassword1");

setupPasswordToggle("id_password2", "togglePassword2");