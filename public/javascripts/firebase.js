(function(req, res) {
    //const firebase=null;
    // Initialize Firebase
    const config = {
        apiKey: "AIzaSyAWe_eDwVTwISgCcCDy5PPxW4bZlq6sHCQ",
        authDomain: "tfg-findegrado.firebaseapp.com",
        databaseURL: "https://tfg-findegrado.firebaseio.com",
        projectId: "tfg-findegrado",
        storageBucket: "tfg-findegrado.appspot.com",
        messagingSenderId: "281469807949"
    };
    // Your web app's Firebase configuration
    /*const config = {
      apiKey: "AIzaSyAxW6tl3dFFm4H1ozmiE9f_ely5TYnKh-k",
      authDomain: "dosjoder-46c0a.firebaseapp.com",
      databaseURL: "https://dosjoder-46c0a.firebaseio.com",
      projectId: "dosjoder-46c0a",
      storageBucket: "",
      messagingSenderId: "817627935482",
      appId: "1:817627935482:web:86486e729b09d4e7"
    };*/
    firebase.initializeApp(config);
    const firestore = firebase.firestore();
    const settings = { timestampsInSnapshots: true };
    firestore.settings(settings);

    const btnClose = document.getElementById("btnClose");

    btnClose.addEventListener('click', () => {
        deleteAllCookies();
        //console.log("uffffff");
        firebase.auth().signOut().then(function() {
            // Sign-out successful.
            event.preventDefault();
            window.location.href = "/";
            console.log("Sign-out successful")

        }).catch(function(error) {
            console.log(" An error happened. Sign-out incorrect")
            // An error happened.
        });
    });

    function deleteAllCookies() {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
    }



}());