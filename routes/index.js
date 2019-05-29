var express = require('express');
var router = express.Router();
var admin = require('firebase-admin');
var path = require('path');
var fs = require('fs');
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
router.get('/menuAdm', function(req, res, next) {
    let url = req.headers.referer;
    let page = takePageName(url);
    //console.log("Vengo de : " + url);
    //console.log("Pagina es: " + page);
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
});
// Promise for verify page.
function verifyOn(url) {
    return new Promise(function(resolve, reject) {
        if (url != undefined) {
            let page = takePageName(url);
            var arrPag = ['menuAdm', 'graphics', 'newAdm', 'deleteAdm', 'newUser', 'deleteUser'];
            //console.info("Verify on dentro : " + arrPag.includes(page)); // true
            let aux = arrPag.includes(page); // true o false.
            //console.info("Verify on dentro aux: " + aux);
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
/* GET userDelete page. */
router.get('/deleteUser', function(req, res, next) {
    let url = req.headers.referer;
    verifyOn(url)
        .then(function(valor) {
            console.log("Inf: Verify page correct");
            if (req.cookies.email == 'root@gmail.com') {
                res.render('deleteUser', { title: titleApp, iam: 'root' });
            } else {
                res.render('deleteUser', { title: titleApp, iam: 'other' });
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

/* GET DeleteUser page. */
router.post('/delUserAd', function(req, res, next) {
    admin.auth().getUserByEmail(req.cookies.deleted)
        .then(function(userRecord) {
            res.clearCookie("deleted");
            // See the UserRecord reference doc for the contents of userRecord.
            admin.auth().deleteUser(userRecord.uid)
                .then(function() {
                    console.log("Successfully deleted admin user");
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

//Promise Start listing users from the beginning, 1000 at a time.v
function listAllAdmUsers(nextPageToken) {
    return new Promise(function(resolve, reject) {
        // List batch of users, 1000 at a time.
        admin.auth().listUsers(1000, nextPageToken)
            .then(function(listUsersResult) {
                const users = new Array();
                listUsersResult.users.forEach(function(userRecord) {
                    //console.log("user", userRecord.toJSON().email);
                    if ("root@gmail.com" != userRecord.toJSON().email) {
                        users.push(userRecord.toJSON().email)
                    }
                    resolve(users)
                });

                if (listUsersResult.pageToken) {
                    resolve(listAllAdmUsers(listUsersResult.pageToken))
                }
            })
            .catch(function(error) {
                console.log("Error listing users:", error);
                reject(error)
            });
    })
}

/* GET deleteAdmin page. */
router.get('/deleteAdm', function(req, res, next) {
    //(admin.auth().getUserByEmail())
    listAllAdmUsers().then(function(users) {
        //console.log(users)
        let url = req.headers.referer;
        verifyOn(url).then(function(valor) {
                //console.log("Inf: Verify page correct");
                if (req.cookies.email == 'root@gmail.com') {
                    res.render('deleteAdm', { title: titleApp, iam: 'root', emailUser: users });
                } else {
                    res.render('error', {
                        title: titleApp,
                        message: "You do not have permission to receive content",
                        error: { status: 401, stack: "Unauthorized" }
                    });
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
    })
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
                console.log("Inf: Verify page incorrect");
                // 401 Unauthorized: no tienes permiso para recibir ese contenido.
                res.render('error', {
                    title: titleApp,
                    message: "You do not have permission to receive content",
                    error: { status: 401, stack: "Unauthorized" }
                });
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
            // console.log("Inf: Verify page correct");
            //videoOn()
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
    //videoOn();

});

function videoOn() {
    //res.render('getIn', { title: titleApp });
    var PythonShell = require('python-shell');
    //pyshell = new PythonShell('sudo ls');
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
}

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
    var dataC = null;
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

function callPython(cmd) {
    var PythonShell = require('python-shell');
    var pyshell = null;
    console.log("Estoy en verify");
    // console.log(req.query.optVerif )
    pyshell = new PythonShell(cmd);

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

    });
    pyshell = null;
}
/* Verify footprint.*/
router.get('/saveFootprint', function(req, res, next) {
    console.log('python ./../bin/mainFootprint.py')
    callPython("python ./../bin/mainFootprint.py")
    res.send({ "code": code, "text": "message" });
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

// Post
router.post('/deleteSelect', function(req, res, next) {
    console.log(req.cookies.datos.split(","))
    let rest = req.cookies.datos.split(",")

    if (rest[0] != "") {
        res.clearCookie("datos");
        deleteFiles(rest)
    }

    setTimeout(res.send({ message: "DeleteSelect Correct" }), 5000);
});

async function deleteFiles(rest) {
    try {
        var datos = 0
        let path_dir_tmp = __dirname
        path_dir_tmp = path.join(path_dir_tmp, "..")
        path_dir_tmp = path.join(path_dir_tmp, "public")
        path_dir_tmp = path.join(path_dir_tmp, "video")
        path_dir_tmp = path.join(path_dir_tmp, "images")

        for (datos; datos < rest.length; datos++) {
            console.log(rest[datos])
            let delelete_new = path.join(path_dir_tmp, rest[datos])
            fs.unlink(delelete_new, (err) => {
                if (err) throw err;
                console.log("Borro")
            });
        }
    } catch {
        console.log("Todo borrado")
    }

}
// Post
router.post('/ordSelect', function(req, res, next) {
    let path_dir_tmp = __dirname
    path_dir_tmp = path.join(path_dir_tmp, "..")
    path_dir_tmp = path.join(path_dir_tmp, "public")
    path_dir_tmp = path.join(path_dir_tmp, "video")
    path_dir_tmp = path.join(path_dir_tmp, "images")

    ord(path_dir_tmp, path_dir_tmp, function(err) {
        console.log(err)
    })

    res.send({ "photos": " files" });

});


async function ord(path_dir_tmp, path_dir_save, callback) {
    try {
        fs.readdir(path_dir_tmp, (err, files) => {
            if (err) throw err;
            let cont = 0
            let ordFiles = files.sort((a, b) => {
                let aa = parseInt(a.split("."));
                let bb = parseInt(b.split("."));
                //aa - bb
                if (aa > bb) {
                    return 1;
                }
                if (aa < bb) {
                    return -1;
                }
                return 0;
            })
            for (const file of ordFiles) {
                cont += 1
                let newName = cont.toString() + ".jpg"
                console.log(file + " = " + newName)
                fs.rename(path.join(path_dir_tmp, file), path.join(path_dir_save, newName), function(err) {
                    if (err) {
                        if (err.code === 'EXDEV') {
                            copy();
                        } else {
                            //cont -= 1
                            callback(err);
                        }
                        return;
                    }

                    callback("fuera");
                });
            }
            callback("su puta madre")

        })
    } catch {
        console.log(err)

    }

    function copy() {
        var readStream = fs.createReadStream(path_dir_tmp);
        var writeStream = fs.createWriteStream(path_dir_save);

        readStream.on('error', callback);
        writeStream.on('error', callback);

        readStream.on('close', function() {
            fs.unlink(path_dir_tmp, callback); // delete todo.
        });

        readStream.pipe(writeStream);
    }




}

function hacerFotos() {
    let path_dir_tmp = __dirname
    path_dir_tmp = path.join(path_dir_tmp, "..")
    path_dir_tmp = path.join(path_dir_tmp, "public")
    path_dir_tmp = path.join(path_dir_tmp, "video")
    path_dir_tmp = path.join(path_dir_tmp, "images")
    // console.log(path_dir_tmp)
    let path_file_face = __dirname
    path_file_face = path.join(path_file_face, "..")
    path_file_face = path.join(path_file_face, "bin")
    path_file_face = path.join(path_file_face, "recognizerVideo")
    path_file_face = path.join(path_file_face, "recognizer")
    path_file_face = path.join(path_file_face, "att_faces")
    path_file_face = path.join(path_file_face, "tmp_face")

    fs.readdir(path_dir_tmp, (err, files) => {

            for (const file of files) {
                fs.rename(file, path_file_face, function(err) {
                    if (err) throw err;
                    fs.stat(path_file_face, function(err, stats) {
                        if (err) throw err;
                        console.log('stats: ' + JSON.stringify(stats));
                    });
                });
            }
        })
    }
    // Post
    router.post('/take_photos', function(req, res, next) {

        // listaa().then(function(){
        //      fs.readdir(path_dir_tmp, (err, files) => {         
        //                 res.send({ "photos": files });
        //                 console.log(files)
        //     })
        // })
        hacerFotos();

        res.send({ "photos": " files" });

        //console.log(__dirname)
        // let path_dir_tmp = __dirname
        // path_dir_tmp = path.join(path_dir_tmp, "..")
        // path_dir_tmp = path.join(path_dir_tmp, "public")
        // path_dir_tmp = path.join(path_dir_tmp, "video")
        // path_dir_tmp = path.join(path_dir_tmp, "images")
        // // console.log(path_dir_tmp)
        // let path_file_face = __dirname
        // path_file_face = path.join(path_file_face, "..")
        // path_file_face = path.join(path_file_face, "bin")
        // path_file_face = path.join(path_file_face, "recognizerVideo")
        // path_file_face = path.join(path_file_face, "recognizer")
        // path_file_face = path.join(path_file_face, "att_faces")
        // path_file_face = path.join(path_file_face, "tmp_face")
        // // path_file_face = path.join(path_file_face, "tmp_face.jpg")
        // //console.log(path_file_face)
        // //mira cantidad de fotos y mover x fotos

        // let cont = 0
        // fs.readdir(path_dir_tmp, (err, files) => {
        //     cont = files.length
        //     //console.log(cont)
        //     let aux = (20 - cont)
        //     //console.log("Tengo k hacer:" + aux)
        //     if (aux > 0) {
        //         take_photos(aux, cont, path_file_face, path_dir_tmp, function(errr) {
        //             if (errr){
        //                 console.log(errr)
        //             } 
        //             console.log(errr)

        //         })
        //         res.send({ "photos": " files" });
        //     } else {
        //         // for (const file of files) {
        //         //     let delelete_new = path.join(path_dir_tmp, file)
        //         //     fs.unlink(delelete_new, (err) => {
        //         //         if (err) throw err;
        //         //         console.log("Borro")
        //         //     });
        //         // }
        //         // take_photos(20, cont, path_file_face, path_dir_tmp, function(errr) {
        //         //     if (errr) throw errr;

        //         // })
        //         res.send({ "photos": " files" });
        //         console.log("esto es una mierdaaa")

        //     }
        // })


    });


    function take_photos(cant_photos, cant_newPath, dir_oldPath, newPath, callback) {

        let cont = cant_newPath
        fs.readdir(dir_oldPath, (err, files) => {
            if (err) throw err;
            cant_photos = cant_photos + cont
            console.log("con :" + cont)
            console.log("foto :" + cant_photos)

            //cont += 1
            // let ordFiles = files.sort((a, b) => {
            //     let aa = parseInt(a.split("."));
            //     let bb = parseInt(b.split("."));
            //     //aa - bb
            //     if (aa > bb) {
            //         return 1;
            //     }
            //     if (aa < bb) {
            //         return -1;
            //     }
            //     return 0;
            // })

            for (const file of files) {
                if (cant_photos > cont) {
                    cont += 1
                    let newName = cont.toString() + ".jpg"
                    console.log(newName)
                    fs.rename(path.join(dir_oldPath, file), path.join(newPath, newName), function(err) {
                        if (err) {
                            if (err.code === 'EXDEV') {
                                copy();
                            } else {
                                cont -= 1
                                callback(err);
                            }
                            return;
                        }

                    });

                } else {

                    return
                }

            }
        })

        function copy() {
            var readStream = fs.createReadStream(dir_oldPath);
            var writeStream = fs.createWriteStream(newPath);

            readStream.on('error', callback);
            writeStream.on('error', callback);

            readStream.on('close', function() {
                fs.unlink(dir_oldPath, callback); // delete todo.
            });

            readStream.pipe(writeStream);
        }
    }
    // Post
    router.post('/confir_photos', function(req, res, next) {
        let name = req.cookies.nombre
        // console.log(__dirname)
        let path_dir_tmp = __dirname
        path_dir_tmp = path.join(path_dir_tmp, "..")
        path_dir_tmp = path.join(path_dir_tmp, "public")
        path_dir_tmp = path.join(path_dir_tmp, "video")
        path_dir_tmp = path.join(path_dir_tmp, "images")
        //console.log(path_dir_tmp)
        let path_dir_save = __dirname
        path_dir_save = path.join(path_dir_save, "..")
        path_dir_save = path.join(path_dir_save, "bin")
        path_dir_save = path.join(path_dir_save, "recognizerVideo")
        path_dir_save = path.join(path_dir_save, "recognizer")
        path_dir_save = path.join(path_dir_save, "att_faces")
        path_dir_save = path.join(path_dir_save, "orl_faces")

        let nameFile = req.cookies.nombre + "_" + req.cookies.newUser.split('@')[0]
        res.cookie('nameFile', nameFile);
        move(nameFile, path_dir_tmp, path_dir_save, function(err) {
            //console.log(err)
        })
        res.send({ "info": "Save Photos" });
    });



    function sendNamePhotoFirebase(name, callback) {

        sendNamePhotoFirebase("holaaa", function() {
            console.log("lo mande")
        })

        var db = admin.firestore();
        var docRef = db.collection('users').doc('alovelace');
        var setAda = docRef.set({
            first: 'Ada',
            last: 'Lovelace',
            born: 1815
        });
        //    var setDoc = admin.firestore().collection('users')
        // Get a database reference to our blog
        // var db = admin.database();
        // var ref = db.ref("/database/firestore/");

        // var usersRef = ref.child("users");
        // usersRef.set({
        //   alanisawesome: {
        //     date_of_birth: "June 23, 1912",
        //     full_name: "Alan Turing"
        //   },
        //   gracehop: {
        //     date_of_birth: "December 9, 1906",
        //     full_name: "Grace Hopper"
        //   }
        //});
        //     setDoc.collection('users').doc("9bzzY0zxnsPibuXtpyFl").update({
        //   "nickname": name
        // });

    }
    // function moveA(dir_oldPath, newPath, callback) {


    //     //console.log(dir_oldPath)
    //     // console.log(newPath)
    //     fs.readdir(dir_oldPath, (err, files) => {
    //         if (err) throw err;

    //         for (const file of files) {
    //             fs.rename(path.join(dir_oldPath, file), path.join(newPath, file), function(err) {
    //                 if (err) {
    //                     if (err.code === 'EXDEV') {
    //                         copy();
    //                     } else {
    //                         // callback(err);
    //                         callback(err);
    //                     }
    //                     return;
    //                 }
    //                 //  callback("Archivo move");
    //                 callback();
    //             });

    //         }
    //     });


    //     function copy() {
    //         var readStream = fs.createReadStream(oldPath);
    //         var writeStream = fs.createWriteStream(newPath);

    //         readStream.on('error', callback);
    //         writeStream.on('error', callback);

    //         readStream.on('close', function() {
    //             // fs.unlink(oldPath, callback); // delete todo.
    //         });

    //         readStream.pipe(writeStream);
    //     }
    // }

    function move(name, dir_oldPath, newPath, callback) {
        newPath = path.join(newPath, name)
        if (!fs.existsSync(newPath)) {
            fs.mkdirSync(newPath); //fs.mkdirSync(newPath, 0744);
        }

        //console.log(dir_oldPath)
        //console.log(newPath)
        fs.readdir(dir_oldPath, (err, files) => {
            if (err) throw err;

            for (const file of files) {
                //let newfile = file + ".pgm" // este camio no rula
                let newfile = file
                fs.rename(path.join(dir_oldPath, file), path.join(newPath, newfile), function(err) {
                    if (err) {
                        if (err.code === 'EXDEV') {
                            copy();
                        } else {
                            //callback(err);
                            callback();
                        }
                        return;
                    }

                    // callback("Archivo move");
                    callback();
                });

            }
        });


        function copy() {
            var readStream = fs.createReadStream(dir_oldPath);
            var writeStream = fs.createWriteStream(newPath);

            readStream.on('error', callback);
            writeStream.on('error', callback);

            readStream.on('close', function() {
                fs.unlink(dir_oldPath, callback); // delete todo.
            });

            readStream.pipe(writeStream);
        }
    }

    module.exports = router;