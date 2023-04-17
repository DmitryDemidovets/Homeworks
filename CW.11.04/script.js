console.log('message')
const textfield = document.getElementById("input") 
console.log(textfield.value)
const BTN = document.getElementById("btn1")
BTN.addEventListener("click", myFunction);
const output = document.getElementById("output")
document.body.onkeyup = function(e) {
     if (e.key == " " ||e.code == "Space" ||e.keyCode == 32 ){
        if (textfield.value==="4"){
            output.innerHTML="True"
        } else{
            output.innerHTML="False"
        }
     }
}
function myFunction() {
    console.log(textfield.value);
    if (textfield.value==="4"){
        output.innerHTML="True"
    } else{
        output.innerHTML="False"
    }

}
