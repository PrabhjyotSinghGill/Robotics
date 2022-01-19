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
    fetch('/startauto/')
            .then(function(response) {
            })
            .then(function(myJson) {
            });

}