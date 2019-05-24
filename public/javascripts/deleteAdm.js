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