(function(req, res) {
    //const firebase=null;
    // Initialize Firebase
    // const config = {
    //   apiKey: "AIzaSyAWe_eDwVTwISgCcCDy5PPxW4bZlq6sHCQ",
    //   authDomain: "tfg-findegrado.firebaseapp.com",
    //   databaseURL: "https://tfg-findegrado.firebaseio.com",
    //   projectId: "tfg-findegrado",
    //   storageBucket: "tfg-findegrado.appspot.com",
    //   messagingSenderId: "281469807949"
    // };

    // firebase.initializeApp(config);
    ///////////////////////////////////////
    var HttpClient = function() {
        this.post = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200 ||
                    anHttpRequest.status == 404) {
                    aCallback(anHttpRequest.response);
                }

            }
            anHttpRequest.open("POST", aUrl, false);
            anHttpRequest.send(null);
        }
    }
    const adminUser = document.getElementById('adminUser');

    /////////////////////////////////////////////////////
    // Obtener elementos
    const clave1 = document.getElementById("inputConfEmail");
    const clave2 = document.getElementById("inputEmail");
    const formDelete = document.getElementById("formDelete");
    // Añadir Evento al formulario
    formDelete.addEventListener('submit', deleteAdm, false);

    // function deleteAdm(event){ 
    //   event.preventDefault(); 
    //   if(verifyEmails()){
    //     var client = new HttpClient();
    //     client.post('/delUserAd', function(response) {          
    //       // console.log(response);
    //       alert(response);     
    //       clave1.value = "";    
    //       clave2.value = "";    
    //     },false);
    //   }
    // }
    function deleteAdm() {
        event.preventDefault();
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                console.log("user:" + user.email)
                // User is signed in.
                var user = firebase.auth().currentUser;

                user.delete().then(function() {
                    // User deleted.
                    
                }).catch(function(error) {
                    // An error happened.
                });
            } else {
                // No user is signed in.
                cosole.log("usurio no")
            }
        });
    }

    function verifyEmails() {
        if ((clave1.value == "") || (clave2.value == "")) {
            return false;
        }
        if ((clave1.value != clave2.value)) {
            clave1.value = "";
            clave2.value = "";
            alert("The emails not equals")
            return false;
        }
        return true;
    }
}());