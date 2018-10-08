var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Secure Access Control' });
});

/* GET admin page. */
router.get('/admin', function(req, res, next) {
  res.render('admin', { title: 'Secure Access Control' });
});

/* GET admin page. */
router.get('/pruebas', function(req, res, next) {
  res.render('pruebas', { title: 'Secure Access Control' });
});

/* GET removeUser page. */
router.get('/removeUser', function(req, res, next) {
  res.render('removeUser', { title: 'Secure Access Control' });
});

/* GET removeAdmin page. */
router.get('/removeAdm', function(req, res, next) {
  res.render('removeAdm', { title: 'Secure Access Control' });
});

/* GET newAdm page. */
router.get('/newAdm', function(req, res, next) {
  console.log("estoy aki")
  res.render('newAdm', { title: 'Secure Access Control' });
});

/* GET newUser page. */
router.get('/newUser', function(req, res, next) {
  console.log("estoy aki")
  res.render('newUser', { title: 'Secure Access Control' });
});

/* GET menuAdm page. */
router.get('/menuAdm', function(req, res, next) {
  console.log(req);
  res.render('menuAdm', { title: 'Secure Access Control' });
});


/* GET getIn page. */
router.get('/graphics', function(req, res, next) {
  res.render('graphics', { title: 'Secure Access Control' });
});

/* GET getIn page. */
router.get('/getIn', function(req, res, next) {
  res.render('getIn', { title: 'Secure Access Control' });
});

/* Post getIn page. */
router.post('/info', function(req, res, next) {
});

// Save footprint and GET menuAdm page.
router.get('/saveFootprint', function(req, res, next) {
  console.log("Estoy en saVeFootprint");  
  var PythonShell = require('python-shell');
  var pyshell = null;
  var dataC=null;
 
  pyshell = new PythonShell('sudo python2 ./../bin/saveFootprint.py');
  pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
      dataC=message;
   });
   // end the input stream and allow the process to exit
   pyshell.end(function (err,code,signal) {
     /// if (err) throw err;
     console.log('The exit err: ' + err);
     console.log('The exit code was: ' + code);
     console.log('The exit signal was: ' + signal);
     //console.log('The opcion: ' + opcion);
     console.log('finished');
     var  message="";
     switch (code) {
	case 1:
	    message = "The fingerprint sensor could not be initialized";
	    break;
        case 2:
	    message  = "Match found!!! Impossible to save. Are you already registered";
	    break;
	default:
	    message  = "Correct Save!!!";		
	    break;
      }   
	// dataC dato cifrado.
        console.log("dataC : "+dataC);
        res.send({"code":code,"text":message,"dataC":dataC});     
   });
   pyshell = null;
});

// Verify footprint.
router.get('/verifyFootprint', function(req, res, next) {
  var PythonShell = require('python-shell');
  var pyshell = null;
  console.log("Estoy en verify");
  // console.log(req.query.optVerif )
  pyshell = new PythonShell('python2 ./../bin/verifyFootprint.py');

  // // if(req.query.optVerif==="footprint" ){
  // //   pyshell = new PythonShell('./bin/verifyFootprint.py');
  // // } else{
  // //   pyshell = new PythonShell('./bin/verifyFace.py');
  // // }
   var opcion = 0;  // Según lo que ocurra en el script de python este valor tendar un numero.
  
  //  envía un mensaje a la secuencia de comandos de Python a través de stdin
  pyshell.send('Valores que recibe python');  // Datos que se le mandan al script.
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
     console.log(message);
     // if(message == "a"){
       //  console.log("Estoy dentro")
        // opcion=20;
      // }
   });
   // end the input stream and allow the process to exit
   pyshell.end(function (err,code,signal) {
     /// if (err) throw err;
     console.log('The exit err: ' + err);
     console.log('The exit code was: ' + code);
     console.log('The exit signal was: ' + signal);
     //console.log('The opcion: ' + opcion);
     console.log('finished');
     var  message="";
     switch (code) {
	case 1:
	    message = "The fingerprint sensor could not be initialized";
	    break;
        case 2:
	    message  = "No match found!!! Repit";
	    break;
	default:
	    message  = "Correct verification!!!";		
	    break;
     }
     res.send({"code":code,"text":message});
   });
   pyshell = null;
});

// Verify Image and GET menuAdm page.
router.get('/verifyImage', function(req, res, next) {
  var PythonShell = require('python-shell');
  var pyshell = null;
  // console.log(req.idPhoto);
  
  console.log("Estoy en verify Image");

  pyshell = new PythonShell('sudo python2 ./../bin/face/verifyFace.py');
     
  //pyshell.send('Valores que recibe python');  // Datos que se le mandan al script.
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
console.log("Estoy dsafdsfdsfy");    
 console.log(message);
   });
   // end the input stream and allow the process to exit
   pyshell.end(function (err,code,signal) {
     /// if (err) throw err;
     console.log('The exit err: ' + err);
     console.log('The exit code was: ' + code);
     console.log('The exit signal was: ' + signal);
     //console.log('The opcion: ' + opcion);
     console.log('finished');
     var  message="";
     switch (code) {
	case 1:
	    message = "Error!!! No foud verify image";
	    break;
        case 2:
	    message  = "No match whith Footprint!!!";
	    break;
	default:
	    message  = "Correct verification!!!";		
	    break;
      }   
	persona = "persona identificada";
 	sistem = "Poner la codificacion de aparato k drei mac pro ejemplo "
 
        res.send({"code":code,"text":message,"persona":persona,"sistem":sistem});
     
   });
   pyshell = null;
});
// Verify Image and GET menuAdm page.
router.get('/saveImage', function(req, res, next) {
  var PythonShell = require('python-shell');
  var pyshell = null;
  // console.log(req.idPhoto);
  
  console.log("Estoy en verify Image");

  pyshell = new PythonShell('python2 ./../bin/face/capture.py '+ "dios");
  pyshell.send('Valores que recibe python');  // Datos que se le mandan al script.
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
     console.log(message);
   });
   // end the input stream and allow the process to exit
   pyshell.end(function (err,code,signal) {
     /// if (err) throw err;
     console.log('The exit err: ' + err);
     console.log('The exit code was: ' + code);
     console.log('The exit signal was: ' + signal);
     //console.log('The opcion: ' + opcion);
     console.log('finished');
     var  message="";
     switch (code) {
	case 1:
	    message = "The fingerprint sensor could not be initialized";
	    break;
        case 2:
	    message  = "No match found!!! Repit";
	    break;
	default:
	    message  = "Correct verification!!!";		
	    break;
      }   
        res.send({"code":code,"text":message});
     
   });
   pyshell = null;
});

module.exports = router;
