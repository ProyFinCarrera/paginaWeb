// Catch buttons
const btnCheckF = document.getElementById("btnCheckF");
const divCheckFRed = document.getElementById("divCheckFRed");
const pCheckFText = document.getElementById("pCheckFText");


setInterval("video()", 30);
//setInterval("infoData()", 2000);
function video() {
    var img = document.getElementById('myImg');
    if (img.complete){
      // img.src = "cam.jpg?" + Math.random();
    }
    // La URL de la imagen es "shenglong.jpg"
    // var img = new Image();
    // img.onload = loadHandler;
    // if (img.complete)
    //     img.onload();
    // var img = document.getElementById('myimg');
    // img.src = "";
    // img.addEventListener("load", loadHandler, false);
    // img.src = "cam.jpg";
}
///////////////////////////////////////
var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200) {
                aCallback(anHttpRequest.response);
            }
        }
        anHttpRequest.open("GET", aUrl, false);
        anHttpRequest.send(null);
    }
}




function infoData() {
    var client = new HttpClient();
    let dir = "/infoR?" + Math.random();
    client.get(dir, function(response) {
        // do something with response
        if (response != null) {
            var content = JSON.parse(response);
            console.log(content['code'])
            if ((content['code'] == "1") && (pCheckFText.innerHTML == "")) {
                text = content['Name'] + " se ha registrado con fecha " + content['date'];
                pCheckFText.innerHTML = text;
                console.log("dentrooo " + content['code'])
                divCheckFRed.style.borderColor = "green";
                divCheckFRed.style.backgroundColor = "green";
                // btnCheckF.disabled = true;
                setTimeout("clear();", 2000);
            }
        }
    });
}

function clear() {
    console.log("Clear")
    divCheckFRed.style.borderColor = "red";
    divCheckFRed.style.backgroundColor = "red";
    pCheckFText.innerHTML = '';
}
