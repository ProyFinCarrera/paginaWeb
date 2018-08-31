const clave1 = document.getElementById("inputConfEmail");
const clave2 = document.getElementById("inputEmail");

function removeAdm(){
  if(comprobarClave()){
    console.log("Remove Adm");
  }
}

function removeUser(){
 if(comprobarClave()){
    console.log("Remove User")
 }
}

function comprobarClave(){ 
    if((clave1.value == "")||( clave2.value=="") ){
   	return false;      
    }
    if ((clave1.value != clave2.value)){             
            clave1.value = "";
            clave2.value = "";
      	    alert("The emails not equals") 
            return false;
    }
   return true;  
} 
