#!/usr/bin/env node
//mport Firebase from 'firebase';
var firebase = require("firebase");


 var config = {
    apiKey: "AIzaSyAWe_eDwVTwISgCcCDy5PPxW4bZlq6sHCQ",
    authDomain: "tfg-findegrado.firebaseapp.com",
    databaseURL: "https://tfg-findegrado.firebaseio.com",
    projectId: "tfg-findegrado",
    storageBucket: "tfg-findegrado.appspot.com",
    messagingSenderId: "281469807949"
  };
firebase.initializeApp(config);
//var imagenSubir = createElement("IMG");
 //var imagenSubir= new Image();
   // imagenSubir.src =  "04.jpg";
var imagenSubir ="04.jpg"
     console.log(imagenSubir);
     console.log(imagenSubir.name)
    storageRef = firebase.storage().ref("imagenes/" + imagenSubir ) // directorio raiz
    // storageRef = firebase.storage.ref()// hijo del direcctorio raiz
    // var uploadTAsk = storageRef.put(imagenSubir)
     
     console.log("Estoy en subir imagen");
 //    console.log(uploadTAsk)
   // console.log("Respuesta" + uploadTAsk)
