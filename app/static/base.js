
function delete_alert(){
   this.parentElement.remove()
}

const collection = document.getElementsByClassName("close");
for (button of collection){
    button.addEventListener("click",delete_alert)
}

