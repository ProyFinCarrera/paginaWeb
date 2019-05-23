(function(req, res) {
    const send = document.getElementById("send");
    send.addEventListener('click', () => {
        makePost();
    })

    function makePost() {
        var client = new HttpClient();
        let dir = "/getIn" + Math.random();
        var client = new HttpClient();
        client.post(dir, function(response) {
            // console.log(response);
            //alert(response);
        }, false);
    }
    var HttpClient = function() {
        this.post = function(aUrl, aCallback) {
            var anHttpRequest = new XMLHttpRequest();
            anHttpRequest.onreadystatechange = function() {
                if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200 ||
                    anHttpRequest.status == 404) {
                    aCallback(anHttpRequest.response);
                }

            }
            anHttpRequest.open("POST", aUrl, false);
            anHttpRequest.send(null);
        }
    }
}());