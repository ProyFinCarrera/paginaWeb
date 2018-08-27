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
const photo = document.getElementById("photo");
const btnTakePhoto = document.getElementById("btnTakePhoto");
const btnOpenDoor = document.getElementById("btnOpenDoor");

const divCheckFRed = document.getElementById("divCheckFRed");
const pCheckFText = document.getElementById("pCheckFText");
const divCheckIRed = document.getElementById("divCheckIRed");
const pCheckIText = document.getElementById("pCheckIText");
    


function clear(){
    console.log("Clear")
    btnCheckF.disabled= false;
    btnCheckI.disabled=true;
    btnTakePhoto.disabled=true;
    btnOpenDoor.disabled=true;
    photo.setAttribute('src', "images/face.png");
    
    // Put red buttons
    divCheckFRed.style.borderColor="red";
    divCheckFRed.style.backgroundColor="red";
    divCheckIRed.style.borderColor="red";
    divCheckIRed.style.backgroundColor="red";
    
    pCheckFText.innerHTML = '';
    pCheckIText.innerHTML = '';
    
}

btnCheckF.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");
    
    
    


    // setTimeout("clear()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.
    // Comprobar que la persona esta. hacer funcion.

    function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}
    var a="";
    var url="https://proy-ultimo-alu0100813272.c9users.io/verify";
    httpGetAsync(url,a);
    
    
    
    pCheckFText.innerHTML = 'Todo correcto!!';
    
    divCheckFRed.style.borderColor="green";
    divCheckFRed.style.backgroundColor="green";
    
    // si esta la persona la imagen ya estar solo 
    btnCheckF.disabled = true;
    
    btnTakePhoto.disabled = false;
    
},true);

 btnTakePhoto.addEventListener('click',()=>{
     btnCheckI.disabled=false;
 });

btnCheckI.addEventListener('click',()=>{
    console.log("Evento accionado boton add Footprint");
  
    
     // Hacer funcional la parate de la huella.
    
    
    pCheckIText.innerHTML = 'Todo correcto!!';
    
    divCheckIRed.style.borderColor="green";
    divCheckIRed.style.backgroundColor="green";
    
    // Imagne no esta desbloqueo. sino solo desbloque el registro.
    btnCheckI.disabled=true;
    btnTakePhoto.disabled=true;
    btnOpenDoor.disabled=false;
},true);
