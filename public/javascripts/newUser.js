var storageRef;  // referencia a la subida de la imagen
console.log("Carga de subir usersss");
      
// service firebase.storage {
//   match /b/{bucket}/o {
//     match /{allPaths=**} {
//       allow read, write: if request.auth != null;
//     }
//   }
// }


// Catch buttons
const btnAddData = document.getElementById("btnAddData");
const btnAddFootprint = document.getElementById("btnAddFootprint");
const btnAddImage = document.getElementById("btnAddImage");
const btnRegister = document.getElementById("btnRegister");


btnAddData.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");
    var divDataRed = document.getElementById("divDataRed");
    var pDataText = document.getElementById("pDataText");
    
    


    setTimeout("location.reload()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.
    // Comprobar que la persona esta. hacer funcion.

    
    
    
    
    pDataText.innerHTML = 'Todo correcto!!';
    
    divDataRed.style.borderColor="green";
    divDataRed.style.backgroundColor="green";
    
    // si esta la persona la imagen ya estar solo 
    btnAddData.disabled = true;
    btnAddFootprint.disabled=false;
    
},true);



btnAddFootprint.addEventListener('click',()=>{
    console.log("Evento accionado boton add Footprint");
    var divFootprintRed = document.getElementById("divFootprintRed");
    var pFootprintText = document.getElementById("pFootprintText");
    
    
     // Hacer funcional la parate de la huella.
    
    
    pFootprintText.innerHTML = 'Todo correcto!!';
    
    divFootprintRed.style.borderColor="green";
    divFootprintRed.style.backgroundColor="green";
    
    // Imagne no esta desbloqueo. sino solo desbloque el registro.
    btnAddFootprint.disabled=true;
    btnAddImage.disabled=false;
},true);

btnAddImage.addEventListener('click',()=>{
     console.log("Evento accionado boton Image");
    var divImageRed = document.getElementById("divImageRed");
    var pImageText = document.getElementById("pImageText");
    
    // manda la imagen a firebase.
    
    
    
    
    
    pImageText.innerHTML = 'Todo correcto!!';
    
    divImageRed.style.borderColor="green";
    divImageRed.style.backgroundColor="green";
    btnAddImage.disabled=true;
    btnRegister.disabled=false;
},true);