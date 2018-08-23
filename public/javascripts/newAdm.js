
 comparacion : (email,confEmail,pass,confPass) =>{
        if (email !== confEmail){
          // alert("Email no soy iguales vuelve a escribir")
          return false;
        }
        if (pass !== confPass){
          // alert("Password no son iguales vuelve escribir")
          return false;
        }
     return true;
    }

 function registrar() {
    
    // Obtener elementos
    console.log("estoy dentro")
  
  const inputEmail = document.getElementById("inputEmail");
  const inputConfEmail = document.getElementById("inputConfEmail");
  const inputPassword = document.getElementById("inputPassword");
  const inputConfPassword = document.getElementById("inputConfPassword");
  const btnSignIn = document.getElementById("btnSignIn");
  
  
  // Obtener email y pass
  const email = inputEmail.value;
  const pass = inputPassword.value;
  const confEmail = inputConfEmail.value;
  const confPass = inputConfPassword.value;
  
  if(comparacion(email, confEmail, pass,confPass)){
    firebase.auth().createUserWithEmailAndPassword(email, pass).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
    });
  }else { 
      console.log("Algo va mal")
      
  }
}
