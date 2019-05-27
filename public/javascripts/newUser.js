(function(req, res) {

    // setTimeout("location.reload()", 5000); // Medri el tiempo para poner esta recaga
    // Poner  un contador cuando presione estoy para refrescar la pagina si pasa x tiempo.

    // Catch input data
    const firstName = document.getElementById("firstName");
    const lastName = document.getElementById("lastName");
    const workPosition = document.getElementById("workPosition");
    const email = document.getElementById("email");
    const otherInfo = document.getElementById("otherInfo");
    const divFootprintRed = document.getElementById("divFootprintRed");
    const pFootprintText = document.getElementById("pFootprintText");
    const divDataRed = document.getElementById("divDataRed");
    const pDataText = document.getElementById("pDataText");
    const divImageRed = document.getElementById("divImageRed");
    const pImageText = document.getElementById("pImageText");

    // Catch buttons 
    const btnAddData = document.querySelector("#btnAddData");
    const btnAddFootprint = document.getElementById("btnAddFootprint");
    const btnAddImage = document.getElementById("btnAddImage");
    const btnTakePhotos = document.getElementById("btnTakePhotos");
    const btnDeleteSelect = document.getElementById("btnDeleteSelect");

    // Cath Formulario
    const form1 = document.getElementById("form1");
    const form2 = document.getElementById("form2");
    const form3 = document.getElementById("form3");

    // Client
    var HttpClient = function() {
        this.get = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200) {
                    aCallback(anHttpRequest.response);
                }
            }
            anHttpRequest.open("GET", aUrl, false);
            anHttpRequest.send();
        }
    }

    // Client Post
    var HttpClient = function() {
        this.post = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200) {
                    aCallback(anHttpRequest.response);
                }
            }
            anHttpRequest.open("POST", aUrl, false);
            anHttpRequest.send();
        }
    }

    // Listener
    form1.addEventListener('submit', addData, false);
    form2.addEventListener('submit', addFootprint, false);
    //form3.addEventListener('submit', addImages, false);


    btnAddImage.addEventListener('click', addImages, false);
    btnTakePhotos.addEventListener('click', takephotos, false);

    btnDeleteSelect.addEventListener('click', deleteSelect, false);

    function deleteSelect() {
        btnDeleteSelect.disabled = true
        btnTakePhotos.disabled = true
        console.log("Eliminarrrrr")

        let aux = []
        let nodo;
        for (nodo = 1; nodo <= 20; nodo++) {
            var myNode = document.getElementById(nodo + ".jpg");
            if (myNode) {
                if (myNode.checked) {
                    aux.push(myNode.value)
                }
            }

        }
        console.log(aux)

        document.cookie = "datos=" + aux;
        limpiar()
        var client = new HttpClient();
        client.post('/deleteSelect', function(response) {
            var content = JSON.parse(response);
            console.log(content.photos)
            var clienta = new HttpClient();
            clienta.post('/ordSelect', function(response) {

                socket.emit("give_pictures", {});
                btnDeleteSelect.disabled = false
                btnTakePhotos.disabled = false
            })



        });
        console.log("Evento accionado boton Image");

    }
 
    const socket = io('http://localhost:3000/video');
    var ctx = document.getElementById('canvas').getContext('2d');
    //socket.emit('give',{})
    socket.on("new_image", function(info) {
        let img = new Image();
        if (info.image) {
            //if(info.buffer.length>0000){
                 if(( info.buffer[ info.buffer.length-5]=="/")||(info.buffer[ info.buffer.length-4]=="/")){
            img.src = 'data:image/jpeg;base64,' + info.buffer;
            //console.log(info.buffer.length)
            img.onload = function() {
                ctx.drawImage(img, 0, 0);
               // socket.emit('give', { image: "ok" })
                img = null
            }
          }

        }
    });

    function limpiar() {
        console.log("Estoy limpiando todo")
        let myNode = document.getElementById("cont_img");
        while (myNode.firstChild) {
            myNode.removeChild(myNode.firstChild);
        }
        var el = document.createElement('div');
        myNode.appendChild(el);
    }


    socket.on("rec_img", function(images) {

        console.log(images);
        images.forEach(function(img) {

            let divI = document.createElement("div")
            divI.setAttribute("class", "form-check form-check-inline")

            let label = document.createElement("label")
            label.setAttribute("class", "form-check-label")
            label.setAttribute("for", "inlineCheckbox1")

            let input = document.createElement("input")
            input.setAttribute("class", "form-check-input")
            input.setAttribute("type", "checkbox")
            input.setAttribute("value", img)
            input.setAttribute("id", img)
         
            let image = document.createElement("img");
            image.setAttribute("src", img + "?" + Math.random());
            image.setAttribute("class", "mw-100 img-responsive")
            image.setAttribute("id", "picture")

            label.appendChild(input)
            divI.appendChild(label)
            divI.appendChild(image)

            var el = document.getElementById('cont_img');

            el.appendChild(divI);

        })
    })


    function deleteCookies(n_cookie) {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            if (name == n_cookie) {
                document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
            }
        }
    }

    function takephotos() {
        btnTakePhotos.disabled = true
        console.log("HAcer fotos")

        limpiar()
        var client = new HttpClient();
        client.post('/take_photos', function(response) {
             var clienta = new HttpClient();
            clienta.post('/ordSelect', function(response) {

                socket.emit("give_pictures", {});
                btnDeleteSelect.disabled = false
                btnTakePhotos.disabled = false
            })

        });
        console.log("Evento accionado boton Image");
    }
   
    function deleteImg() {
        if (!imagen) {
            alert("El elemento selecionado no existe");
        } else {
            padre = imagen.parentNode;
            padre.removeChild(imagen);
        }
    }
    // Function
    function addImages(event) {
        //event.preventDefault();
        console.log("TErminar")
        //document.cookie = "nombre=" + firstName.value;
        document.cookie = "nombre=" + firstName.value;
        var client = new HttpClient();
        client.post('/confir_photos', function(response) {
            // do something with response
            // var content = JSON.parse(response);
            // pCheckFText.innerHTML = content['text'];
            // if (content['code'] == "0") {
            //     divCheckFRed.style.borderColor = "green";
            //     divCheckFRed.style.backgroundColor = "green";
            //     btnCheckF.disabled = true;
            //     btnCheckI.disabled = false;
            // }
            console.log(response)
            socket.emit("give_pictures", {});
        });
        console.log("Evento accionado botonasimagne");
    }

    function addFootprint(event) {
        event.preventDefault();
        setTimeout(upFootprint, 50);
        document.cookie = "newUser=" + email.value;
        pFootprintText.innerHTML = "";
    }


    function addData(event) {
        event.preventDefault();
        setTimeout(upDate(firstName.value, lastName.value, workPosition.value, email.value, otherInfo.value), 50);
        pDataText.innerHTML = "";
    }


    // Send data
    // function upPicture() {
    //     var client = new HttpClient();
    //     client.get('/saveImage', function(response) {
    //         // do something with response
    //         var content = JSON.parse(response);
    //         pCheckFText.innerHTML = content['text'];
    //         if (content['code'] == "0") {
    //             divCheckFRed.style.borderColor = "green";
    //             divCheckFRed.style.backgroundColor = "green";
    //             btnCheckF.disabled = true;
    //             btnCheckI.disabled = false;
    //         }
    //     });
    //     console.log("Evento accionado boton Image");
    //     console.log("dato en imagen: " + nameImage)
    //     // manda la imagen a firebase.

    //     pImageText.innerHTML = 'Todo correcto!!';

    //     divImageRed.style.borderColor = "green";
    //     divImageRed.style.backgroundColor = "green";
    //     btnAddImage.disabled = true;
    //     btnRegister.disabled = false;
    // }

    function upFootprint() {
        var client = new HttpClient();
        // console.log("Evento accionado boton add data");
        console.log("Evento accionado boton add Footprint");
        //Hacer funcional la parate de la huella.
        client.get('/saveFootprint', function(response) {
            // do something with response
            var content = JSON.parse(response);
            pFootprintText.innerHTML = content['text'];
            if (content['code'] == "0") {

                divFootprintRed.style.borderColor = "green";
                divFootprintRed.style.backgroundColor = "green"

                // Imagne no esta desbloqueo. sino solo desbloque el registro.
                btnAddFootprint.disabled = true;
                btnAddImage.disabled = false;

                nameImage = content['dataC'];

                mando = { datoC: nameImage }
                console.log(nameImage);

                emaila = "nuevo@gmail.com";
                // console.log(content['dataC']);
                upDataC(mando, emaila);

            }
            console.log(response);
        });
    }

    function upDate(firstName, lastName, workPosition, email, otherInfo) {
        // Initialize Cloud Firestore through Firebase
        let db = firebase.firestore();
        // Create a query against the collection
        let userdb = db.collection("users").where('emailId', '==', email).get()
            .then(function(querySnapshot) {
                if (querySnapshot.empty) {
                    sendDataFerestore(firstName, lastName, workPosition, email, otherInfo);
                    alert("New registered user");
                    console.log('No documents found');
                    pDataText.innerHTML = 'Todo correcto!!';
                    divDataRed.style.borderColor = "green";
                    divDataRed.style.backgroundColor = "green";
                    btnAddData.disabled = true;
                    btnAddFootprint.disabled = false;
                    otherInfo.disabled = false;
                    blockInput();
                } else {
                    // do something with the data 
                    if (confirmNewDivice()) {
                        pDataText.innerHTML = 'Todo correcto!!';
                        divDataRed.style.borderColor = "green";
                        divDataRed.style.backgroundColor = "green";
                        btnAddData.disabled = true;
                        btnAddFootprint.disabled = false;
                        blockInput();

                    } else {
                        clearInput();
                    }
                }
            }).catch(function(error) {
                // console.log("Error getting documents: ", error);
            });
    }

    function sendDataFerestore(firstName, lastName, workPosition, email, otherInfo) {
        let userData;
        if (otherInfo == "") {
            userData = {
                emailId: email,
                firstName: firstName,
                lastName: lastName,
                workPosition: workPosition,
            };
        } else {
            userData = {
                emailId: email,
                firstName: firstName,
                lastName: lastName,
                workPosition: workPosition,
                otherInfo: otherInfo,
            };

        }
        // Initialize Cloud Firestore through Firebase
        let db = firebase.firestore();
        db.collection("users").add(userData)
            .then(function(docRef) {
                console.log("Document written with ID: ", docRef.id);
                docRef.update({ id: docRef.id });

            }).catch(function(error) {
                console.error("Error adding document: ", error);
            });
    }

    // function help
    function clearInput() {
        firstName.value = "";
        lastName.value = "";
        workPosition.value = "";
        email.value = "";
        if (otherInfo.value != "") {
            otherInfo.value = "";
        }
    }

    function blockInput() {
        firstName.disabled = true;
        lastName.disabled = true;
        workPosition.disabled = true;
        email.disabled = true;
        otherInfo.disabled = true;
    }

    function confirmNewDivice() {
        var mensaje = confirm("This user exists, if you want to register the user on you shall proceed to the next item on. Do you want to continue?");
        if (mensaje) {
            return true;
        } else {
            return false;
        }
    }












    // function upDataC(dataC, email) {
    //     // Initialize Cloud Firestore through Firebase
    //     let emails = "soy_yo000@hotmail.com"
    //     let db = firebase.firestore();
    //     // Create a query against the collection
    //     let userdb = db.collection("users").where('emailId', '==', email).get()
    //         .then(function(querySnapshot) {
    //             //console.log("Query");
    //             let id = null;
    //             querySnapshot.forEach(function(doc) {
    //                 // doc.data() is never undefined for query doc snapshots
    //                 console.log(doc.id, " => ", doc.data());
    //                 id = doc.id;
    //             });

    //             if (querySnapshot.empty) {
    //                 console.log('Documents no found');
    //                 alert("User no exists");

    //             } else {
    //                 // do something with the data 
    //                 console.log('Documents found');
    //                 alert("This user exists, add new data.");
    //                 //id ="o8lMusW7GXmf7P4qA3lN";
    //                 sendDataCFerestore(dataC, id);

    //                 let divDataRed = document.getElementById("divDataRed");
    //                 let pDataText = document.getElementById("pDataText");
    //                 console.log('No documents found');
    //                 alert("New registered user");
    //                 pDataText.innerHTML = 'Todo correcto!!';
    //                 divDataRed.style.borderColor = "green";
    //                 divDataRed.style.backgroundColor = "green";
    //                 btnAddData.disabled = true;
    //                 btnAddFootprint.disabled = false;
    //             }
    //         })
    //         .catch(function(error) {
    //             console.log("Error getting documents: ", error);
    //         });

    // }

    // function sendDataCFerestore(dataC, docId) {
    //     //let userData = dataC;
    //     let userData = { caca: "tpafsdfas" };
    //     // Initialize Cloud Firestore through Firebase
    //     let db = firebase.firestore();

    //     db.collection("users").doc(docId).update(dataC)
    //         .then(function() {
    //             console.log("Document successfully updated!");
    //         });

    // }

    // function subirImagen() {
    //     var canvas = document.getElementById("canvas");
    //     canvas.toBlob(function(blob) {
    //         //aquí la variable blob contiene el blob que se acaba de generar
    //         storageRef = firebase.storage().ref("/imagenes/" + "ufffdd.png"); // directorio raiz  
    //         var uploadTAsk = storageRef.put(blob);
    //         console.log("Estoy en subir imagen");
    //         console.log("Respuesta" + uploadTAsk);
    //     });
    // }
}());