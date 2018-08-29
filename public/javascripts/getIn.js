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

// buscar la foto
const imgPhoto = document.getElementById("imgPhoto");

function clear(){
    console.log("Clear")
    btnCheckF.disabled= false;
    btnCheckI.disabled=true;
    btnTakePhoto.disabled=true;
    btnOpenDoor.disabled=true;
    imgPhoto.setAttribute('src', "images/face.png");
    
    // Put red buttons
    divCheckFRed.style.borderColor="red";
    divCheckFRed.style.backgroundColor="red";
    divCheckIRed.style.borderColor="red";
    divCheckIRed.style.backgroundColor="red";
    
    pCheckFText.innerHTML = '';
    pCheckIText.innerHTML = '';
    
}
///////////////////////////////////////
var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {  
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200){
                 aCallback(anHttpRequest.response);
            }
	 
       }
       anHttpRequest.open( "GET", aUrl,false );            
       anHttpRequest.send();	
    }
}
/////////////////////////////////////////////////////



btnCheckF.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");
    // setTimeout("clear()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.
    // Comprobar que la persona esta. hacer funcion.

//    var client = new HttpClient();
//    client.get('/verifyFootprint', function(response) {
       // do something with response
 //       var content = JSON.parse(response);      
 //       pCheckFText.innerHTML =content['text'];
 //       if(content['code'] == "0"){
	//    divCheckFRed.style.borderColor="green";
//	    divCheckFRed.style.backgroundColor="green";
//	    btnCheckF.disabled = true;
//	    btnTakePhoto.disabled = false;
  //      }
   // });
//////////////////quitar estoooo
   divCheckFRed.style.borderColor="green";
	    divCheckFRed.style.backgroundColor="green";
	    btnCheckF.disabled = true;
	    btnTakePhoto.disabled = false;
///////////////////////////////////

},true);

 btnTakePhoto.addEventListener('click',()=>{
     btnCheckI.disabled=false;
 });

btnCheckI.addEventListener('click',()=>{
    console.log("Evento accionado boton add Image");
    //strDrawableB64 = imgPhoto;
   // strDrawableB64.substring(strDrawableB64.indexOf(",")+1);


    var client = new HttpClient();
   // console.log(imgPhoto.src)
    // envoi de la fotoo
    client.get('/verifyImage', function(response) {
       // do something with response
       
    });
   
     // Hacer funcional la parate de la huella.
    
    
    //pCheckIText.innerHTML = 'Todo correcto!!';
    
    //divCheckIRed.style.borderColor="green";
    //divCheckIRed.style.backgroundColor="green";
    
    // Imagne no esta desbloqueo. sino solo desbloque el registro.
   // btnCheckI.disabled=true;
   // btnTakePhoto.disabled=true;
    //btnOpenDoor.disabled=false;
},true);
