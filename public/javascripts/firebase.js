(function(req,res){
  
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
  firebase.initializeApp(config);
 
  // Obtener elementos
  const inputEmail = document.getElementById("inputEmail");
  const inputPassword = document.getElementById("inputPassword");
  const btnSignIn = document.getElementById("btnSignIn");
  
  const cookies = null;
  // Añadir Evento login
  btnSignIn.addEventListener('click', e=>{
     
      // Obtener email y pass
      const email = inputEmail.value;
      const pass = inputPassword.value;
      
      const auth = firebase.auth();
        console.log("fsdafds");
      const promise = auth.signInWithEmailAndPassword(email, pass);
      cookies = promise;
      console.log("antes");
       console.log(promise);
      promise.catch( e=> console.log(e.message ));
  });
 
  console.log(firebase);

}());