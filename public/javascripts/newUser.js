var storageRef;  // referencia a la subida de la imagen
console.log("Carga de subir usersss");
      
// service firebase.storage {
//   match /b/{bucket}/o {
//     match /{allPaths=**} {
//       allow read, write: if request.auth != null;
//     }
//   }
// }

//Catch input data
const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const workPosition = document.getElementById("workPosition");
const email = document.getElementById("email");
const otherInfo = document.getElementById("otherInfo");

// Catch buttons
const btnAddData = document.querySelector("#btnAddData");// mirear esta mirerda
const btnAddFootprint = document.getElementById("btnAddFootprint");
const btnAddImage = document.getElementById("btnAddImage");
//const btnRegister = document.getElementById("btnRegister");

//////////////////////////////////////////////////////////////////

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
btnAddData.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");

    var divDataRed = document.getElementById("divDataRed");
    var pDataText = document.getElementById("pDataText");
    


    //setTimeout("location.reload()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.
    // Comprobar que la persona esta. hacer funcion.

 
    subirDatos();
    
    
    
    
    pDataText.innerHTML = 'Todo correcto!!';
    
    divDataRed.style.borderColor="green";
    divDataRed.style.backgroundColor="green";
    
    // si esta la persona la imagen ya estar solo 
    btnAddData.disabled = true;
    btnAddFootprint.disabled=false;
    
},true);


function subirDatos(){
    storageRef = firebase.database().ref(); // directorio raiz	
    console.log("Estoy Subinedo Datos.");
    // crar json.
    var json={"datos":[{"nombre" :''},{"apellido":''},{"ciudad":''}]};
    var obj = JSON.parse(json);
    console.log(obj);
    var uploadTAsk = storageRef.push(json);     
    console.log("Respuesta" + uploadTAsk);
}




var nameImage = null;
btnAddFootprint.addEventListener('click',()=>{
    console.log("Evento accionado boton add Footprint");
    var divFootprintRed = document.getElementById("divFootprintRed");
    var pFootprintText = document.getElementById("pFootprintText");
  
    // Hacer funcional la parate de la huella.
    var client = new HttpClient();
    client.get('/saveFootprint', function(response) {
       // do something with response
        var content = JSON.parse(response); 
        pFootprintText.innerHTML = content['text'];
        if(content['code'] == "0"){
	  divFootprintRed.style.borderColor="green";
          divFootprintRed.style.backgroundColor="green";
          // Imagne no esta desbloqueo. sino solo desbloque el registro.
          btnAddFootprint.disabled=true;
          btnAddImage.disabled=false;
          nameImage = content['dataC'];
        }
        console.log(response);
    }); 
},true);


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
       anHttpRequest.send(null);	
    }
}
/////////////////////////////////////////////////////


btnAddImage.addEventListener('click',()=>{
    
    var client = new HttpClient();
    client.get('/saveImage', function(response) {
      // do something with response
       var content = JSON.parse(response);      
       pCheckFText.innerHTML =content['text'];
       if(content['code'] == "0"){
            divCheckFRed.style.borderColor="green";
	    divCheckFRed.style.backgroundColor="green";
	    btnCheckF.disabled = true;
	    btnCheckI.disabled = false;
        }
   });



    console.log("Evento accionado boton Image");
    var divImageRed = document.getElementById("divImageRed");
    var pImageText = document.getElementById("pImageText");
    console.log("dato en imagen: " + nameImage)
    // manda la imagen a firebase.

    
    pImageText.innerHTML = 'Todo correcto!!';
    
    divImageRed.style.borderColor="green";
    divImageRed.style.backgroundColor="green";
    btnAddImage.disabled=true;
    btnRegister.disabled=false;
},true);

function subirImagen(){
    var canvas = document.getElementById("canvas");
    canvas.toBlob(function(blob) {
       //aquí la variable blob contiene el blob que se acaba de generar
       storageRef = firebase.storage().ref("/imagenes/" + "ufffdd.png" ); // directorio raiz	
       var uploadTAsk = storageRef.put(blob);     
       console.log("Estoy en subir imagen");
       console.log("Respuesta" + uploadTAsk);
    });
}
    
const btnRegister = document.getElementById("btnRegister");
btnRegister.addEventListener('click',()=>{
    console.log("Evento accionado boton add data");
    subirImagen();
},true);

