let text11=document.getElementById("cell11");
let text12=document.getElementById("cell12");
let text13=document.getElementById("cell13");
let text14=document.getElementById("cell14");

var socket = io.connect(
    location.protocol + "//" + document.domain + ":" + location.port
  );





    socket.emit("request_progress");
    socket.on("update-progress-event", function (data) {
      console.log(data.img1);
      text11.innerHTML=data.cell11;
      text12.innerHTML=data.cell12;
      text13.innerHTML=data.cell13;
      text14.innerHTML=data.cell14;
      socket.emit("request_progress");
      });

//setInterval(function () {request_progress_from_server();}, 100);




function setModeManual(){

        fetch('/setmode/?m=Manual')
                .then(function(response) {
                })
                .then(function(myJson) {
                });
 document.getElementById("manualSection").disabled = false;
 document.getElementById("autoSection").disabled = true;
 document.getElementById("navbarDarkDropdownMenuLink").innerHTML = "<b>Manual</b>";
}
function setModeAuto(){
        fetch('/setmode/?m=Auto')
                .then(function(response) {
                })
                .then(function(myJson) {
                });
 document.getElementById("manualSection").disabled = true;
 document.getElementById("autoSection").disabled = false;
 document.getElementById("navbarDarkDropdownMenuLink").innerHTML = "<b>Auto</b>";
}
function setInsertionOperation(){
        fetch('/setmanualoperation/?o=Insertion')
                .then(function(response) {
                })
                .then(function(myJson) {
                });
        document.getElementById("dropdownMenuButton1").innerHTML = "Insertion";

}
function setCrimpingOperation(){
        fetch('/setmanualoperation/?o=Crimping')
                .then(function(response) {
                })
                .then(function(myJson) {
                });
        document.getElementById("dropdownMenuButton1").innerHTML = "Crimping";
}
function startManual(){

        fetch('/startmanual/')
                .then(function(response) {
                })
                .then(function(myJson) {
                });

                }
function startAuto(){
        fetch('http://127.0.0.1:5002/startrobot/')
                .then(function(response) {
                })
                .then(function(myJson) {
                });

}
function forceQuit(){
        fetch('http://127.0.0.1:5002/haltrobot/')
                .then(function(response) {
                })
                .then(function(myJson) {
                });
}