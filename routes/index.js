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
router.get('/getIn', function(req, res, next) {
  res.render('getIn', { title: 'Secure Access Control' });
});

// Verify footprint and GET menuAdm page.
router.get('/verify', function(req, res, next) {
  var PythonShell = require('python-shell');
  var pyshell = null;
  console.log(req.query.optVerif )
  if(req.query.optVerif==="footprint" ){
    pyshell = new PythonShell('./bin/verifyFootprint.py');
  } else{
    pyshell = new PythonShell('./bin/verifyFace.py');
  }
  var opcion = 0;  // Según lo que ocurra en el script de python este valor tendar un numero.
  
  //  envía un mensaje a la secuencia de comandos de Python a través de stdin
  pyshell.send('Valores que recibe python');  // Datos que se le mandan al script.
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
      if(message == "a"){
        console.log("Estoy dentro")
        opcion=20;
      }
  });
  // end the input stream and allow the process to exit
  pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit err: ' + err);
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('The opcion: ' + opcion);
    console.log('finished');
    
  });
  //pyshell = null;
  res.render('getIn', { title: 'Secure Access Control' });
});


module.exports = router;
