(function(req,res){
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

  // Obtener elementos
  const inputEmail = document.getElementById("inputEmail");
  const inputConfEmail = document.getElementById("inputConfEmail");
  const inputPassword = document.getElementById("inputPassword");
  const inputConfPassword = document.getElementById("inputConfPassword");
  //const btnSignIn = document.getElementById("btnSignIn");
  
  const formSign = document.getElementById("formSign");
  // Añadir Evento al formulario
  formSign.addEventListener('submit', registrar, false);
  
  function registrar(event){ 
    // Cancela evento.
    event.preventDefault(); 
    if(comprobarPassword()&&comprobarEmail() ){  
        firebase.auth().createUserWithEmailAndPassword(inputEmail.value,inputPassword.value)
        .then(function(value){
          console.log(value);
          inputEmail.value = "";
          inputConfEmail.value = "";
          inputPassword.value = "";
          inputConfPassword.value = "";
          alert("Created new user administrator");
        })
        .catch(function(error) 		{
          // Errors here.
          inputEmail.value = "";
          inputConfEmail.value = "";
          inputPassword.value = "";
          inputConfPassword.value = "";
          // Vemos el error
          alert(error.message);
        });
    }
  }

  function comprobarEmail() {
    console.log("comprobarEmail");
    if((inputEmail.value == "")||( inputConfEmail.value=="") ){
     	return false;      
    }
    if ((inputEmail.value != inputConfEmail.value)){             
      inputEmail.value = "";
      inputConfEmail.value = "";
      inputPassword.value = "";
      inputConfPassword.value = "";
      alert("The emails not equals") 
      return false;
    }
    return true;  
  }

  function comprobarPassword() {
    console.log("comprobarPassword");
     if((inputPassword.value == "")||( inputConfPassword.value=="") ){
     	return false;      
      }
      if ((inputPassword.value != inputConfPassword.value)){             
              inputPassword.value = "";
              inputConfPassword.value = "";
              inputEmail.value = "";
              inputConfEmail.value = "";
        	    alert("The passports not equals") 
              return false;
      }
     return true;  
  }
}());