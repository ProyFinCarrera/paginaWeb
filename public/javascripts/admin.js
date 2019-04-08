(function(req, res) {
    // Obtener elementos
    const inputEmail = document.getElementById("inputEmail");
    const inputPassword = document.getElementById("inputPassword");
    const btnSignIn = document.getElementById("btnSignIn");
    const formSign = document.getElementById("formSign");

    formSign.addEventListener('submit', login, false);

    function login(event) {
        event.preventDefault();
        var email = inputEmail.value;
        const pass = inputPassword.value;
        console.log("login");
        const promise = firebase.auth().signInWithEmailAndPassword(email, pass).then(function(value) {
            document.cookie = "email=" + email;
            document.cookie = "pass=" + pass;
            // console.log(value);
            inputEmail.value = "";
            window.location.href = "/menuAdm";
        }).catch(function(error) {
            window.location.href = "";
            alert(error.message);
        })
    }
}());