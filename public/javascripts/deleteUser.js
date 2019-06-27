(function(req, res) {
    var HttpClient = function() {
        this.post = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200 ||
                    anHttpRequest.status == 404) {
                    aCallback(anHttpRequest.response);
                }

            }
            anHttpRequest.open("Post", aUrl, false);
            anHttpRequest.send(null);
        }
    }

    const firestore = firebase.firestore();
    const settings = { timestampsInSnapshots: true };
    firestore.settings(settings);
    
    /////////////////////////////////////////////////////
    const clave1 = document.getElementById("inputConfEmail");
    const clave2 = document.getElementById("inputEmail");
    const formDelete = document.getElementById("formDelete");

    formDelete.addEventListener('submit', deleteAdm, false);

    function deleteAdm(event) {
        event.preventDefault();
        let resol = verifyEmails()
        if (resol == true) {
            document.cookie = "deleted=" + clave1.value;
            let client = new HttpClient();
            client.post('/delUserAd', function(response) {
                if (response['code'] == "200") {
                    clave2.remove(clave2.selectedIndex);
                }
                alert(response)
                // console.log(response)
                clave2.selectedIndex = 0;
                clave1.value = "";
            })
        }
    }

    function userDownload() {
         let userdb = firestore.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(doc => {
                let option = document.createElement("option");
                option.value = doc.data().emailId
                option.text = doc.data().emailId;
                clave2.add(option);
                // console.log(doc.data().emailId);
            });
        })
    }
    window.onload=userDownload();        
    function tableUserDownload() {
         let cont = 0 
         let userdb = firestore.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(doc => {

                let tr = document.createElement("tr");
                let th = document.createElement("th");
                th.setAttribute("scope", "row");
                cont+=1
                th.innerHTML = cont
                let td = document.createElement("td");
                td.innerHTML =  doc.data().firstName

                let td1 = document.createElement("td");
                td1.innerHTML =  doc.data().lastName

                let td2 = document.createElement("td");
                td2.innerHTML =  doc.data().emailId
                
                let td3 = document.createElement("td");
                td3.innerHTML =  doc.data().workPosition

                tr.appendChild(th);
                tr.appendChild(td);  
                tr.appendChild(td1);  
                tr.appendChild(td2);  
                tr.appendChild(td3);  

                let tableBody = document.getElementById('tableBody');
                tableBody.appendChild(tr);
            });
        })
    }
    window.onload = tableUserDownload();
    
    function verifyEmails() {
        if ((clave1.value != clave2.value)) {
            clave1.value = "";
            clave2.selectedIndex = 0;
            alert("Email no equal")
            return false;
        } else {
            return true;
        }
    }
}());