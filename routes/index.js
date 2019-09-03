const express = require('express');
const router = express.Router();
const admin = require('firebase-admin');
const path = require('path');
const fs = require('fs');
var ip = require("ip");
const serviceAccount = require('./serviceAccountKey.json');
const titleApp = 'Secure Access Control'
const dir_images = catch_dir_img()
const dir_save = catch_dir_video()
const dir_faces = catch_dir_faces()
/* Function to take the address of the image folder */
function catch_dir_img() {
    let path_tmp = __dirname;
    path_tmp = path.join(path_tmp, "..");
    path_tmp = path.join(path_tmp, "public");
    path_tmp = path.join(path_tmp, "video");
    path_tmp = path.join(path_tmp, "images");
    return path_tmp;
}
/* Function to take the address of the video folder */
function catch_dir_faces() {
    let path_tmp = __dirname
    path_tmp = path.join(path_tmp, "..")
    path_tmp = path.join(path_tmp, "bin")
    path_tmp = path.join(path_tmp, "recognizerVideo")
    path_tmp = path.join(path_tmp, "recognizer")
    path_tmp = path.join(path_tmp, "att_faces")
    path_tmp = path.join(path_tmp, "tmp_faces")
    return path_tmp;
}
/* Function to take the address of the  folder */
function catch_dir_video() {
    let path_tmp = __dirname
    path_tmp = path.join(path_tmp, "..")
    path_tmp = path.join(path_tmp, "bin")
    path_tmp = path.join(path_tmp, "recognizerVideo")
    path_tmp = path.join(path_tmp, "recognizer")
    path_tmp = path.join(path_tmp, "att_faces")
    path_tmp = path.join(path_tmp, "orl_faces")
    return path_tmp;
}
/* Initialize connection with firebase */
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: 'https://tfg-findegrado.firebaseio.com'
});
/* GET home page. */
router.get('/', function(req, res, next) {
    let url = req.headers.referer;
    var ip_a = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    

    let page = takePageName(url);
    if((page == "getIn")||(page == "newUser") ){
      closeSistem();
    }
    if((ip_a.split(":")[3] ==  ip.address())||(ip_a.split(":")[2] == "1")){
        res.render('index', { title: 'Secure Access Control', out:false });
    }else{
       res.render('index', { title: 'Secure Access Control', out:true });
    }
   
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
    if (page == "newUser") {
      closeSistem()
    }
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
    let page = takePageName(url);
    if (page == "newUser") {
      closeSistem()
    }
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
    let url = req.headers.referer;
    let page = takePageName(url);
    if (page == "newUser") {
      closeSistem()
    }
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
    let page = takePageName(url);
    if (page == "newUser") {
      closeSistem()
    }
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
function closeSistem(){
     // Initialize verification process
        var PythonShell = require('python-shell');
        //pyshell = new PythonShell('sudo ls');
        pyshell = new PythonShell('sudo python ./../bin/close.py');
        pyshell.on('message', function(message) {
            // received a message sent from the Python script (a simple "print" statement)
            console.log(message);
        });
        pyshell.end(function(err, code, signal) {
            /// if (err) throw err;
            console.log('The exit err: ' + err);
            console.log('The exit code was: ' + code);
            console.log('The exit signal was: ' + signal);
            //console.log('The opcion: ' + opcion);
            console.log('finished');
        });
        pyshell = null;
}
/* GET newUser page. */
router.get('/newUser', function(req, res, next) {
    let url = req.headers.referer;
    let aux_out = true
    let ip_a = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    
    if((ip_a.split(":")[3] ==  ip.address())||(ip_a.split(":")[2] == "1")){
        aux_out =false
    }
    let page = takePageName(url);   
    verifyOn(url)
        .then(function(valor) {
             if (page != "newUser") {
            // console.log("Inf: Verify page correct");
            //videoOn()
            // Initialize verification process
            var PythonShell = require('python-shell')
            //pyshell = new PythonShell('sudo python ./../bin/mainSaveFaceNew.py');
            pyshell = new PythonShell('sudo python ./../bin/saveFaceWeb.py');
            //pyshell = new PythonShell('sudo python ./../bin/mainSaveFace.py');
            pyshell.on('message', function(message) {
                // received a message sent from the Python script (a simple "print" statement)
                console.log(message);
                dataC = message;
            });
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
            if(aux_out!=true){
                if (req.cookies.email == 'root@gmail.com') {

                    res.render('newUser', { title: titleApp, iam: 'root'});
                } else {

                    res.render('newUser', { title: titleApp, iam: 'other'});
                }
            }else{
                  res.render('error', {
                title: titleApp,
                message: "Operation no permiti: only on the device.",
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
/* GET getIn page. */
router.get('/graphics', function(req, res, next) {
    let url = req.headers.referer;
    let page = takePageName(url);
    if (page == "newUser") {
      closeSistem()
    }
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
    let url = req.headers.referer;
    let page = takePageName(url);
    res.render('getIn', { title: titleApp });
    if (page != "getIn") {
        
        var PythonShell = require('python-shell');
        //pyshell = new PythonShell('sudo python ./../bin/mainNew.py');
        pyshell = new PythonShell('sudo python ./../bin/recognizerWeb.py', { args: [req.cookies.newUser] });
        //pyshell = new PythonShell('sudo python3 ./../bin/main.py');
        pyshell.on('message', function(message) {
            // received a message sent from the Python script (a simple "print" statement)
            console.log(message);
            dataC = message;
        });
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
});
/* Save footprint and GET menuAdm page.
router.post('/saveFootprint', function(req, res, next) {
    let path_file = __dirname
    path_file = path.join(path_file, "./..")
    path_file = path.join(path_file, "bin")
    path_file = path.join(path_file, 'mainSaveFootprint.py')
    console.log(req.cookies)

    //res.send({})
    var PythonShell = require('python-shell');
    pyshell = new PythonShell('sudo python ./../bin/mainSaveFootprint.py', { args: [req.cookies.newUser] });
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
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
                message = "The fingerprint sensor could not be initialized";
                break;
            case 2:
                message = "Match found!!! Impossible to save. Are you already registered";
                break;
            default:
                message = "All right!!!";
                break;
        }
        res.send({ "code": code, "message": message });
    });
    pyshell = null;
});*/

// Post
router.post('/deleteSelect', function(req, res, next) {
    //console.log(req.cookies.datos.split(","))
    let rest = req.cookies.datos.split(",")
    if (rest[0] != "") {
        res.clearCookie("datos");
        deleteFiles(rest)
    }

    res.send({ message: "DeleteSelect Correct" })
});

// Post
router.post('/deleteUserSystem', function(req, res, next) {
    //res.send({})
    var PythonShell = require('python-shell');
    pyshell = new PythonShell('sudo python ./../bin/deletedAll.py', { args: [req.cookies.nameFile] });
    pyshell.on('message', function(message) {
        // received a message sent from the Python script (a simple "print" statement)
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
            case 0:
 		message = "All right!!!";
                break;
            default:
                message = "Error Deleted user";
                break;
            
               
        }
        res.send({ "code": code, "message": message });
    });
    pyshell = null;
});


async function deleteFiles(rest) {
    try {
        var datos = 0
        let path_dir_tmp = dir_images

        for (datos; datos < rest.length; datos++) {
            // console.log(rest[datos])
            let delelete_new = path.join(path_dir_tmp, rest[datos])
            fs.unlink(delelete_new, (err) => {
                if (err) throw err;
                //console.log("Borro")
            });
        }
    } catch {
        console.log("Not clear")
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
        //console.log(err)

    })
    res.send({ message: "Order Correct" })
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
                // console.log(file + " = " + newName)
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

                    callback();
                });
            }
            callback()

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

// Post
router.post('/take_photos', function(req, res, next) {
    //hacerFotos()
    //res.send({ "photos": " files" });
    let cont = 0
    fs.readdir(dir_images, (err, files) => {
        cont = files.length
        //console.log(cont)
        let aux = (20 - cont)
        //console.log("Tengo k hacer:" + aux)
        if (aux > 0) {
            take_photos(aux, cont, dir_faces, dir_images, function(errr) {
                if (errr) {
                    console.log(errr)
                }
                console.log(errr)

            })

        } else {
            // for (const file of files) {
            //     let delelete_new = path.join(path_dir_tmp, file)
            //     fs.unlink(delelete_new, (err) => {
            //         if (err) throw err;
            //         console.log("Borro")
            //     });
            // }
            // take_photos(20, cont, path_file_face, path_dir_tmp, function(errr) {
            //     if (errr) throw errr;

            // })
            // res.send({ "photos": " files" });
            

        }
        res.send({ message: "Take Photos Correct" })
    })
});

function take_photos(cant_photos, cant_newPath, dir_oldPath, newPath, callback) {

    let cont = cant_newPath
    fs.readdir(dir_oldPath, (err, files) => {
        if (err) throw err;
        cant_photos = cant_photos + cont
        //console.log("con :" + cont)
        //console.log("foto :" + cant_photos)
        for (const file of files) {
            if (cant_photos > cont) {
                cont += 1
                let newName = cont.toString() + ".jpg"
                // console.log(newName)
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
    try {
        let name = req.cookies.nombre
        let nameFile = req.cookies.nombre + "_" + req.cookies.newUser.split('@')[0]
        res.cookie('nameFile', nameFile);
        move(nameFile, dir_images, dir_save, function(err) {
            //console.log(err)
        })
        res.send({ code: "0", message: "All right!!!" });
    } catch {
        res.send({ code: "1", message: "Save Error!!!" });
    }
});




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
