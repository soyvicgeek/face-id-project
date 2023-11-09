document.getElementById("toggle-password").onclick = function () {
    let claveInput = document.getElementById("clave");
    if (claveInput.type === "password") {
        claveInput.type = "text";
        this.classList.remove("fa-eye-slash");
        this.classList.add("fa-eye");
    } else {
        claveInput.type = "password";
        this.classList.remove("fa-eye");
        this.classList.add("fa-eye-slash");
    }
};
