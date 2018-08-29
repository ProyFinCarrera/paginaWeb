(function startVideo() {
   var streaming = false,
      video        = document.querySelector('#video'),
      cover        = document.querySelector('#cover'),
      canvas       = document.querySelector('#canvas'),
      photo        = document.querySelector('#imgPhoto'),
      startbutton  = document.querySelector('#btnTakePhoto');
  navigator.getMedia = ( navigator.getUserMedia || 
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia);

     

  navigator.getMedia(
    { 
      video: true, 
      audio: false 
    },
    function(stream) {
       
      if (navigator.mozGetUserMedia) { 
        video.mozSrcObject = stream;
        
      } else {
        var vendorURL = window.URL || window.webkitURL;
        video.src = vendorURL ? vendorURL.createObjectURL(stream) : stream;
      }
      
      video.play();
   
    },
    function(err) {
      console.log("An error occured! " + err);
    }
  );

   function draw() {
        var canvas = document.getElementById('canvas');
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');

    ctx.beginPath();
    ctx.arc(75,75,50,0,Math.PI*2,true); // Círculo externo
    ctx.moveTo(110,75);
    ctx.arc(75,75,35,0,Math.PI,false);   // Boca (contra reloj)
    ctx.moveTo(65,65);
    ctx.arc(60,65,5,0,Math.PI*2,true);  // Ojo izquierdo
    ctx.moveTo(95,65);
    ctx.arc(90,65,5,0,Math.PI*2,true);  // Ojo derecho
    ctx.stroke();
  }
}
  function takepicture() {
    canvas.width = photo.width;
    canvas.height = photo.height;
    canvas.getContext('2d').drawImage(video, 0, 0, photo.width, photo.height);
    var data = canvas.toDataURL('images');
    photo.setAttribute('src', data);
    
    // apartir de aki mandar la foto para arriba la nuve.
    console.log(photo)///
   
  }

  btnTakePhoto.addEventListener('click', function(ev){
      takepicture();
      ev.preventDefault();
  }, false);
 var btnCheckImagen  = document.querySelector('#btnCheckImagen');/// ai Imagen btnCheckI? par inde
btnCheckI.addEventListener('click',()=>{
    console.log("Evento accionado boton add Image");
    //strDrawableB64 = imgPhoto;
   // strDrawableB64.substring(strDrawableB64.indexOf(",")+1);


    var client = new HttpClient();
   // console.log(imgPhoto.src)
    // envoi de la fotoo

   client.post('/verifyImage', function(response) {
       // do something with response
		console.log(response);
       
    });
    
},true);

///////////////////////////////////////
var HttpClient = function() {
    this.post = function(aUrl,aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {  
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200){
                 aCallback(anHttpRequest.response);
            }
	 
       }
       var formData = new FormData();
       formData.append("afile", imgPhoto.file);
       console.log(formData);

       anHttpRequest.open( "POST", aUrl+ "?data=" +"{\'file\':"+formData+"}",true );          
       anHttpRequest.send(formData);
	
    }
}
})();
