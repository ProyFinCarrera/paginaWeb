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
    // const btnAddData = document.getElementById("btnAddData");
    const btnAddFootprint = document.getElementById("btnAddFootprint");
    const btnAddImage = document.getElementById("btnAddImage");
    const btnTakePhotos = document.getElementById("btnTakePhotos");
    const btnDeleteSelect = document.getElementById("btnDeleteSelect");
    const btnSelectAll = document.getElementById("btnSelectAll");

    // Client Get
    var HttpClientGet = function() {
        this.get = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200) {
                    aCallback(anHttpRequest.response);
                }
            }
            anHttpRequest.open("GET", aUrl, true);
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
            anHttpRequest.open("POST", aUrl, true);
            anHttpRequest.send();
        }
    }
    const form1 = document.getElementById("form1");
    // btnAddData.addEventListener('click', addData, false);
    form1.addEventListener('submit', addData, false);
    btnAddFootprint.addEventListener('click', addFootprint, false);
    btnAddImage.addEventListener('click', addImages, false);
    btnTakePhotos.addEventListener('click', takephotos, false);
    btnDeleteSelect.addEventListener('click', deleteSelect, false);
    btnSelectAll.addEventListener('click', selectAll, false);

    var socket = io('http://localhost:3000/video',{ reconnection: false });
    //var socket = io('http://192.168.1.42:3000/video');//{ reconnection: false }
    //var socket = io('http://192.168.1.50:3000/video', { reconnection: false });
    //var ctx = document.getElementById('canvas').getContext('2d');
   
    setTimeout( function videoOn() {
        let img = document.getElementById('canvas');
        img.src = 'http://localhost:8000/stream.mjpg';
    } ,8000)

    socket.on("rec_img", function(images) {
        clearDiv();
        images.forEach(function(img) {
            let divI = document.createElement("div");
            switch (images.length) {
                case 3:
                    divI.setAttribute("class", "form-check form-check-inlin col-4");
                    break;
                case 2:
                    divI.setAttribute("class", "form-check form-check-inlin col-6");
                    break;
                case 1:
                    divI.setAttribute("class", "form-check form-check-inlin col-12")
                    break;
                default:
                    divI.setAttribute("class", "form-check form-check-inlin col-3");
            }

            let label = document.createElement("label");
            label.setAttribute("class", "form-check-label");
            label.setAttribute("for", "inlineCheckbox1");

            let input = document.createElement("input");
            input.setAttribute("class", "form-check-input check");
            input.setAttribute("type", "checkbox");
            input.setAttribute("value", img);
            input.setAttribute("id", img);

            let image = document.createElement("img");
            image.setAttribute("src", img + "?" + Math.random());
            image.setAttribute("class", "mw-100 img-responsive");
            image.setAttribute("id", "picture");

            label.appendChild(input);
            divI.appendChild(label);
            divI.appendChild(image);

            let divF = document.getElementById('cont_img');
            divF.appendChild(divI);
        })

        btnDeleteSelect.disabled = false;
        if (images.length < 20) {
            btnTakePhotos.setAttribute("class", "btn-sm btn-success my-button col-3")
            btnTakePhotos.disabled = false;
            btnAddImage.disabled = true;
        } else {
            btnTakePhotos.setAttribute("class", "btn-sm btn-outline-success my-button col-3");
            btnAddImage.disabled = false;
        }
    })

    function clearDiv() {
        let myNode = document.getElementById("cont_img");
        while (myNode.firstChild) {
            myNode.removeChild(myNode.firstChild);
        }
    }

    function selectAll() {
        //console.log("Sleccion")
        sel = document.getElementById("cont_img").getElementsByTagName('input');
        // console.log(sel.length);
        for (var i = 0; i < sel.length; i++) {
            sel[i].checked = true;
        }

    }

    function refresh() {
        //console.log("HAcer refresh")
        deleteDataFirebase(); // elimino el domengo
        clearDiv(); // elimina todo als foto del 3 formulario
        //console.log(document.cookie.DOCREF);
        deleteCookies("DOCREF");
        var client = new HttpClient();
        client.post('/refresh', function(response) {
            // elimar de la base de datos todo los reqistros.
            // mandar nombre y buscar la capeta si esta borrarla.
            // elimnar la huell poss de la huella se va paano dpro cookis
        });
        console.log("Clear All");
    }

    function deleteSelect() {
        btnDeleteSelect.disabled = true
        btnTakePhotos.disabled = true
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
        //console.log(aux)
        document.cookie = "datos=" + aux;
        var client = new HttpClient();
        client.post('/deleteSelect', function(response) {
            var content = JSON.parse(response);
            var clienta = new HttpClient();
            sleep(250); //250
            clienta.post('/ordSelect', function(response) {
                sleep(500); //500
                socket.emit("give_pictures", {})

            })
        });
        //console.log("Evento accionado boton Image");
    }

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

    function readCookie(name) {
        return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + name.replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
    }

    function sleep(milliseconds) {
        var start = new Date().getTime();
        for (var i = 0; i < 1e7; i++) {
            if ((new Date().getTime() - start) > milliseconds) {
                break;
            }
        }
    }

    function deleteUserSystem() {
        var client = new HttpClient();
        client.post('/deleteUserSystem', function(response) {

        });
    }

    function takephotos() {
        btnTakePhotos.disabled = true;
        btnDeleteSelect.disabled = true;
        var client = new HttpClient();
        client.post('/take_photos', function(response) {
            var client2 = new HttpClient();
            // setTimeout(waitGive(), 3000);
            sleep(250);
            client2.post('/ordSelect', function(response) {
                sleep(500);
                socket.emit("give_pictures", {});
            })
        });
        //console.log("Evento accionado takephotos");
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
        event.preventDefault();
        //console.log("AddImages")
        //console.log(firstName.value)
        document.cookie = "nombre=" + firstName.value;
        document.cookie = "newUser=" + email.value;
        var client = new HttpClient();
        client.post('/confir_photos', function(response) {
            // do something with response
            var content = JSON.parse(response);
            pImageText.innerHTML = content['message'];
            if (content['code'] == "0") {
                divImageRed.style.borderColor = "green";
                divImageRed.style.backgroundColor = "green";
                btnAddImage.disabled = true;
                btnAddFootprint.disabled = false;
                btnSelectAll.disabled = true;
                btnDeleteSelect.disabled = true;
            }
            clearDiv();
            sendDataImg();
        });
        //console.log("Evento accionado botonasimagne");
    }

    function sendDataImg() {
        //console.log(readCookie("email"))
        let nameFile = readCookie("nameFile");
        let docRef = readCookie("DOCREF")

        let subir = '{"nameFile":"' + nameFile + '"}'
        // console.log(subir)
        var content = JSON.parse(subir);
        // Initialize Cloud Firestore through Firebase
        let db = firebase.firestore();
        db.collection("users").doc(docRef).update(content).then(function(doc) {
            // console.log("Document written with ID: ");
            // docRef.update({ id: docRef.id });
        }).catch(function(error) {
            console.error("Error adding document: ", error);
        });
    }

    function addData(event) {
        event.preventDefault();
        setTimeout(upDate(firstName.value, lastName.value, workPosition.value, email.value, otherInfo.value), 50);
        pDataText.innerHTML = "";
    }

    //////////////////////////////////////////////////////////falta esto para adeltne

    function addFootprint(event) {
        btnAddFootprint.disabled = true;
        event.preventDefault();      
        pFootprintText.innerHTML = "";
        upFootprint()
    }
    
    
    function upFootprint() {
        var client = new HttpClient();
        //console.log(email.value)
        document.cookie = "newUser=" + email.value; // se crera cuadno la fotos /saveFootprint
        //Hacer funcional la parate de la huella.
        val = "?" + email.value;
        client.post('http://localhost:8000/footprintSave' + val, function(response) {
            // do something with response
            //btnAddFootprint.disabled = false;
            //console.log(response)
            var content = JSON.parse(response);
            setTimeout(writeDatoF, 10, content.message)
            if (content['code'] == "0") {
                divFootprintRed.style.borderColor = "green";
                divFootprintRed.style.backgroundColor = "green";
            } else {
                btnAddFootprint.disabled = false;
            }
        });

    }
    
    function writeDatoF(dato) {
        pFootprintText.innerHTML = dato;
    }

    function upDate(firstName, lastName, workPosition, email, otherInfo) {
        // Initialize Cloud Firestore through Firebase
        let db = firebase.firestore();
        //console.log("update")
        // Create a query against the collection
        let userdb = db.collection("users").where('emailId', '==', email).get()
            .then(function(querySnapshot) {
                if (querySnapshot.empty) {
                    sendDataFirestore(firstName, lastName, workPosition, email, otherInfo);
                    alert("New registered user");
                    console.log('No documents found');
                    pDataText.innerHTML = 'ALL right!!';
                    divDataRed.style.borderColor = "green";
                    divDataRed.style.backgroundColor = "green";
                    btnAddData.disabled = true;
                    btnTakePhotos.disabled = false;
                    btnSelectAll.disabled = false;
                    btnDeleteSelect.disabled = false;
                    blockInput();
                } else {
                    // do something with the data 
                    if (confirmNewDivice()) {
                        pDataText.innerHTML = 'ALL right!!';
                        divDataRed.style.borderColor = "green";
                        divDataRed.style.backgroundColor = "green";
                        btnAddData.disabled = true;
                        btnTakePhotos.disabled = false;
                        btnAddFootprint.disabled = false;
                        btnSelectAll.disabled = false;
                        btnDeleteSelect.disabled = false;
                        blockInput();

                    } else {
                        clearInput();
                    }
                }
            }).catch(function(error) {
                // console.log("Error getting documents: ", error);
            });
    }

    function sendDataFirestore(firstName, lastName, workPosition, email, otherInfo) {
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
                //console.log("Document written with ID: ", docRef.id);
                docRef.update({ id: docRef.id });
                document.cookie = "DOCREF=" + docRef.id;
            }).catch(function(error) {
                console.error("Error adding document: ", error);
            });
    }

    function deleteDataFirebase() {
        // Initialize Cloud Firestore through Firebase
        let DOCREF = document.cookie.DOCREF
        let db = firebase.firestore();
        db.collection("users").doc(DOCREF).delete().then(function() {
            console.log("Document successfully deleted!");
        }).catch(function(error) {
            console.error("Error removing document: ", error);
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
}());
