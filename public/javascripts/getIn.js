 console.log("EStoy akii");
// module.exports ={  
    
//     comparacion : (email,confEmail,pass,confPass) =>{
//         if (email !== confEmail){
//           // alert("Email no soy iguales vuelve a escribir")
//           return false;
//         }
//         if (pass !== confPass){
//           // alert("Password no son iguales vuelve escribir")
//           return false;
//         }
//     return true;
//     }
// }



// Catch buttons
const btnCheckF = document.getElementById("btnCheckF");
const btnCheckI = document.getElementById("btnCheckI");
const btnOpenDoor = document.getElementById("btnOpenDoor");

btnCheckF.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");
    var divCheckFRed = document.getElementById("divCheckFRed");
    var pCheckFText = document.getElementById("pCheckFText");
    
    


    setTimeout("location.reload()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.
    // Comprobar que la persona esta. hacer funcion.

    
    
    
    
    pCheckFText.innerHTML = 'Todo correcto!!';
    
    divCheckFRed.style.borderColor="green";
    divCheckFRed.style.backgroundColor="green";
    
    // si esta la persona la imagen ya estar solo 
    btnCheckF.disabled = true;
    btnCheckI.disabled=false;
    
},true);



btnCheckI.addEventListener('click',()=>{
    console.log("Evento accionado boton add Footprint");
    var divCheckIRed = document.getElementById("divCheckIRed");
    var pCheckIText = document.getElementById("pCheckIText");
    
    
     // Hacer funcional la parate de la huella.
    
    
    pCheckIText.innerHTML = 'Todo correcto!!';
    
    divCheckIRed.style.borderColor="green";
    divCheckIRed.style.backgroundColor="green";
    
    // Imagne no esta desbloqueo. sino solo desbloque el registro.
    btnCheckI.disabled=true;
    btnOpenDoor.disabled=false;
},true);
