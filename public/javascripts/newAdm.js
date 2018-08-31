// Obtener elementos
const inputEmail = document.getElementById("inputEmail");
const inputConfEmail = document.getElementById("inputConfEmail");
const inputPassword = document.getElementById("inputPassword");
const inputConfPassword = document.getElementById("inputConfPassword");
const btnSignIn = document.getElementById("btnSignIn");

function registrar(){
console.log("dentrjo")
   if(comprobarPassword()&&comprobarEmail() ){
      
firebase.auth().createUserWithEmailAndPassword(inputEmail.value,inputPassword.value).catch(function(error) 		{
      // Handle Errors here.
         inputEmail.value = "";
         inputConfEmail.value = "";
         inputPassword.value = "";
         inputConfPassword.value = "";
         alert("Nuw user")
         console.log("dsaffds");
         var errorCode = error.code;
         var errorMessage = error.message;
     });
   }
}
function comprobarEmail() {
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




