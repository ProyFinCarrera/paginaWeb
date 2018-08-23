function registrar(){
    // Obtener elementos
console.log("estoy dentro")
  const inputEmail = document.getElementById("inputEmail");
  const inputPassword = document.getElementById("inputPassword");
  const btnSignIn = document.getElementById("btnSignIn");
  const cookies = null;
  // Obtener email y pass
  const email = inputEmail.value;
  const pass = inputPassword.value;
  firebase.auth().createUserWithEmailAndPassword(email, pass).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
  });
}



var storageRef;  // referencia a la subida de la imagen
//////////////////////
function ficheroSubirImagen(){
    
    var fichero = document.getElementById("imagen");
     console.log(fichero.file)
    var imagenSubir = fichero;
    console.log(imagenSubir.name)
    storageRef = firebase.storage.ref() // directorio raiz
    storageRef = firebase.storage.ref()// hijo del direcctorio raiz
    var uploadTAsk = storageRef.child("imagenes/" + imagenSubir.name).put(imagenSubir)

    console.log("Respuesta" + uploadTAsk)
}