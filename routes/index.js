var express = require('express');
var router = express.Router();
var admin = require('firebase-admin');
var serviceAccount = require('./serviceAccountKey.json');
var titleApp = 'Secure Access Control'
/* Initialize connection with firebase */
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: 'https://tfg-findegrado.firebaseio.com'
});
/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { title: 'Secure Access Control' });
});
/* GET admin page. */
router.get('/admin', function(req, res, next) {
    res.render('admin', { title: titleApp });
});
/* Function */
function takePageName(url) {
    if (url != undefined) {
        return url.replace("?", "").split('/').pop();
    } else {
        return "page";
    }
}
/* GET menuAdm page. */
router.get('/cam', function(req, res, next) {
    console.log("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    res.render('cam', { title: titleApp, iam: 'root' });
});

/* GET menuAdm page. */
router.get('/menuAdm', function(req, res, next) {
    let url = req.headers.referer;
    let page = takePageName(url);
    console.log("Vengo de : " + url);
    console.log("Pagina es: " + page);
    if (page == "admin") {
        if (req.cookies.email == 'root@gmail.com') {
            res.render('menuAdm', { title: titleApp, iam: 'root' });
        } else {
            res.render('menuAdm', { title: titleApp, iam: 'other' });
        }
    } else {
        // 401 Unauthorized: no tienes permiso para recibir ese contenido.
        res.render('error', {
            title: titleApp,
            message: "You do not have permission to receive content",
            error: { status: 401, stack: "Unauthorized" }
        });
    }
    // ver k vengo  de menuAdm ver si las pagin vien todo de menu
    // o enter todo lade menu de grafic o de nose k mierda//
    // de admin  de ningna otra pueden llegar
    // si estoy ya en menuAdm soy un usuario registrado//
});
// Promise for verify page.
function verifyOn(url) {
    return new Promise(function(resolve, reject) {
        if (url != undefined) {
            let page = takePageName(url);
            var arrPag = ['menuAdm', 'graphics', 'newAdm', 'deleteAdm', 'newUser', 'removeUser'];
            console.info("Verify on dentro : " + arrPag.includes(page)); // true
            let aux = arrPag.includes(page); // true o false.
            console.info("Verify on dentro aux: " + aux);
            if (aux == true) {
                return resolve(true);
            } else {
                return reject(false);
            }
        } else {
            return reject(false);
        }
    })
}
/* GET DeleteUser page. */
router.post('/delUserAd', function(req, res, next) {
    admin.auth().getUserByEmail("a@fdas.com")
        .then(function(userRecord) {
            // See the UserRecord reference doc for the contents of userRecord.
            admin.auth().deleteUser(userRecord.uid)
                .then(function() {
                    console.log("Successfully deleted user");
                    // 200 OK
                    res.status(200).send("Successfully deleted user");
                })
                .catch(function(error) {
                    console.log("Error deleting user:", error);
                    // Error 404 Not found
                    res.status(404).send(error.message);
                });
        })
        .catch(function(error) {
            console.log("Error deleting user:", error);
            // Error 404 Not found
            res.status(404).send(error.message);
        });
});
/* GET DeleteUser page. */
router.get('/removeUser', function(req, res, next) {
    let url = req.headers.referer;
    verifyOn(url)
        .then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                res.render('removeUser', { title: titleApp, iam: 'root' });
            } else {
                res.render('removeUser', { title: titleApp, iam: 'other' });
            }
        })
        .catch(function() {
            console.log("Inf: Verify page incorrect");
            // 401 Unauthorized: no tienes permiso para recibir ese contenido.
            res.render('error', {
                title: titleApp,
                message: "You do not have permission to receive content",
                error: { status: 401, stack: "Unauthorized" }
            });
        });
});


function listAllUsers(nextPageToken) {
    admin.auth().listUsers(1000, nextPageToken)
        .then(function(listUsersResult) {
            var users = new Array();
            listUsersResult.users.forEach(function(userRecord) {

                console.log("user", userRecord.toJSON().email);

                users.push(userRecord.toJSON().email)



            });

            if (listUsersResult.pageToken) {
                // List next batch of users.
                //res.render('deleteAdm', { title: titleApp, iam: 'root', emailUser: users });
                //console.log("user", listUsersResult.pageToken);
                listAllUsers(listUsersResult.pageToken)

            }

        })
        .catch(function(error) {
            console.log("Error listing users:", error);
        });
}



/* GET deleteAdmin page. */
router.get('/deleteAdm', function(req, res, next) {

    //(admin.auth().getUserByEmail()
    // Start listing users from the beginning, 1000 at a time.
    //listAllUsers();

    let url = req.headers.referer;
    verifyOn(url).then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                //console.log(users)
                users = { "email": "jaior" }
                res.render('deleteAdm', { title: titleApp, iam: 'root', emailUser: users });
            } else {
                users = { "email": "jaior" }
                res.render('deleteAdm', { title: titleApp, iam: 'other', emailUser: users });
            }
        })
        .catch(function() {
            console.log("Inf: Verify page incorrect");
            // 401 Unauthorized: no tienes permiso para recibir ese contenido.
            res.render('error', {
                title: titleApp,
                message: "You do not have permission to receive content",
                error: { status: 401, stack: "Unauthorized" }
            });
        });
});
/* GET newAdm page. */
router.get('/newAdm', function(req, res, next) {
    let url = req.headers.referer;
    verifyOn(url)
        .then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                res.render('newAdm', { title: titleApp, iam: 'root' });
            } else {
                res.render('newAdm', { title: titleApp, iam: 'other' });
            }
        })
        .catch(function() {
            console.log("Inf: Verify page incorrect");
            // 401 Unauthorized: no tienes permiso para recibir ese contenido.
            res.render('error', {
                title: titleApp,
                message: "You do not have permission to receive content",
                error: { status: 401, stack: "Unauthorized" }
            });
        });
});
/* GET newUser page. */
router.get('/newUser', function(req, res, next) {
    let url = req.headers.referer;
    verifyOn(url)
        .then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                res.render('newUser', { title: titleApp, iam: 'root' });
            } else {
                res.render('newUser', { title: titleApp, iam: 'other' });
            }
        })
        .catch(function() {
            console.log("Inf: Verify page incorrect");
            // 401 Unauthorized: no tienes permiso para recibir ese contenido.
            res.render('error', {
                title: titleApp,
                message: "You do not have permission to receive content",
                error: { status: 401, stack: "Unauthorized" }
            });
        });
});
/* GET getIn page. */
router.get('/graphics', function(req, res, next) {
    let url = req.headers.referer;
    verifyOn(url)
        .then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                res.render('graphics', { title: titleApp, iam: 'root' });
            } else {
                res.render('graphics', { title: titleApp, iam: 'other' });
            }
        })
        .catch(function() {
            console.log("Inf: Verify page incorrect");
            // 401 Unauthorized: no tienes permiso para recibir ese contenido.
            res.render('error', {
                title: titleApp,
                message: "You do not have permission to receive content",
                error: { status: 401, stack: "Unauthorized" }
            });
        });
});

/* GET getIn page. */
router.get('/getIn', function(req, res, next) {
    // Initialize verification process
    res.render('getIn', { title: titleApp });
    var PythonShell = require('python-shell');
    //pyshell = new PythonShell('sudo python ./../bin/main.py');
    pyshell = new PythonShell('sudo python ./../bin/main.py');
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
        dataC = message;
    });


    // pyshell.on('message', function (message) {
    //     // received a message sent from the Python script (a simple "print" statement)
    //     console.log(message);
    // });
    //  // end the input stream and allow the process to exit
    pyshell.end(function(err, code, signal) {
        /// if (err) throw err;
        console.log('The exit err: ' + err);
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        //console.log('The opcion: ' + opcion);
        console.log('finished');
        var message = "";
    });
    pyshell = null;
});

/* GET infoR page. */
router.get('/infoR', function(req, res, next) {
    var fs = require('fs');
    var infoR = require('./../public/infoRegistro/infoR.json');
    res.send(infoR);

    // console.log(infoR);
    // var jsonData = JSON.stringify(infoR);



    // if (infoR.code = "1") {
    //     infoR.code = "0";
    // }
    // jsonData = { "jairo": "dasaf" }
    // console.log(jsonData);

    // fs.open("./public/infoRegistro/infoRa.json")

    // fs.writeFile("./public/infoRegistro/infoRa.json", jsonData, function(err) {
    //     if (err) {
    //         console.log(err);
    //     }
    // });
    // infoR = null;

});
/* Save footprint and GET menuAdm page. */
// router.get('/saveFootprint', function(req, res, next) {
//    console.log("Estoy en saVeFootprint");
//    var data = {
//   name: 'Los Angeles',
//   state: 'CA',
//   country: 'USA'
// };

// // Add a new document in collection "cities" with ID 'LA'
// var setDoc = admin.firestore().collection('users').doc().set(data);
//  admin.firestore().collection('users').doc().set(data);

// var citiesRef = admin.firestore().collection('users');
// var query = citiesRef.where('emailId', '==', "alu01@gmail.com").get()
//     .then(snapshot => {
//       snapshot.forEach(doc => {
//         console.log(doc.data());
//       });
//     })
//     .catch(err => {
//       console.log('Error getting documents', err);
//     });
//    res.send({ "code": "Perfecto", "text": "Sigue asi", "dataC":  "Dale caña" });
// })

/* Save footprint and GET menuAdm page. */
router.get('/saveFootprint', function(req, res, next) {
    console.log("Estoy en saVeFootprint");
    
    console.log(req.cookies.newUser)
    var user = req.cookies.newUser;
    var dataC=null;
     var PythonShell = require('python-shell');
    //pyshell = new PythonShell('sudo python ./../bin/s.py');
    // pyshell = new PythonShell('sudo python ./../bin/main.py');
    pyshell = new PythonShell('sudo python bin/savefootprint.py adsf');
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
        dataC = message;
    });

    // end the input stream and allow the process to exit
    pyshell.end(function(err, code, signal) {
        /// if (err) throw err;
        console.log('The exit err: ' + err);
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        //console.log('The opcion: ' + opcion);
        console.log('finished');
        var message = "";
        switch (code) {
            case 1:
                message = "The fingerprint sensor could not be initialized";
                break;
            case 2:
                message = "Match found!!! Impossible to save. Are you already registered";
                break;
            default:
                message = "Correct Save!!!";
                break;
        }
        // dataC dato cifrado.
        console.log("dataC : " + dataC);

        res.send({ "code": code, "text": message, "dataC": dataC });
    });
    pyshell = null;

});

/* Verify footprint.*/
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
    var opcion = 0; // Según lo que ocurra en el script de python este valor tendar un numero.

    //  envía un mensaje a la secuencia de comandos de Python a través de stdin
    pyshell.send('Valores que recibe python'); // Datos que se le mandan al script.
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
        // if(message == "a"){
        //  console.log("Estoy dentro")
        // opcion=20;
        // }
    });
    // end the input stream and allow the process to exit
    pyshell.end(function(err, code, signal) {
        /// if (err) throw err;
        console.log('The exit err: ' + err);
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        //console.log('The opcion: ' + opcion);
        console.log('finished');
        var message = "";
        switch (code) {
            case 1:
                message = "The fingerprint sensor could not be initialized";
                break;
            case 2:
                message = "No match found!!! Repit";
                break;
            default:
                message = "Correct verification!!!";
                break;
        }
        res.send({ "code": code, "text": message });
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
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log("Estoy dsafdsfdsfy");
        console.log(message);
    });
    // end the input stream and allow the process to exit
    pyshell.end(function(err, code, signal) {
        /// if (err) throw err;
        console.log('The exit err: ' + err);
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        //console.log('The opcion: ' + opcion);
        console.log('finished');
        var message = "";
        switch (code) {
            case 1:
                message = "Error!!! No foud verify image";
                break;
            case 2:
                message = "No match whith Footprint!!!";
                break;
            default:
                message = "Correct verification!!!";
                break;
        }
        persona = "persona identificada";
        sistem = "Poner la codificacion de aparato k drei mac pro ejemplo "

        res.send({ "code": code, "text": message, "persona": persona, "sistem": sistem });

    });
    pyshell = null;
});
// Verify Image and GET menuAdm page.
router.get('/saveImage', function(req, res, next) {
    var PythonShell = require('python-shell');
    var pyshell = null;
    // console.log(req.idPhoto);
    console.log(document.cookiees);
    console.log("Estoy en verify Image");

    // pyshell = new PythonShell('python2 ./../bin/face/capture.py ' + "dios");
    // pyshell.send('Valores que recibe python'); // Datos que se le mandan al script.
    // pyshell.on('message', function(message) {
    //     // received a message sent from the Python script (a simple "print" statement)
    //     console.log(message);
    // });
    // // end the input stream and allow the process to exit
    // pyshell.end(function(err, code, signal) {
    //     /// if (err) throw err;
    //     console.log('The exit err: ' + err);
    //     console.log('The exit code was: ' + code);
    //     console.log('The exit signal was: ' + signal);
    //     //console.log('The opcion: ' + opcion);
    //     console.log('finished');
    //     var message = "";
    //     switch (code) {
    //         case 1:
    //             message = "The fingerprint sensor could not be initialized";
    //             break;
    //         case 2:
    //             message = "No match found!!! Repit";
    //             break;
    //         default:
    //             message = "Correct verification!!!";
    //             break;
    //     }
    //     res.send({ "code": code, "text": message });

    // });
    // pyshell = null;
});

module.exports = router;