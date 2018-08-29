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
  }

  btnTakePhoto.addEventListener('click', function(ev){
      takepicture();
      ev.preventDefault();
  }, false);


})();
