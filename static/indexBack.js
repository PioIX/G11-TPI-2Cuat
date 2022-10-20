id=0

function Busqueda(){
  tags = document.getElementById("barra").value;
  id = id+1
  if(id < 6){
      if(tags.length >= 2){
      document.getElementById("barra").value = "";
        x = id
        console.log(id)
      document.getElementById("tags").innerHTML += `
     <button type='button' value='${tags}' class="but" id=${id} onclick='borrarTag("${x}" )'>${tags} ✖️</button>
    `
      console.log(tags)
    }else{
      console.log("debe tener al menos 2 letras")
      document.getElementById("barra").value = "";
      id = id - 1
    }
    
  }else{
    console.log("hay demasiados tags")
    document.getElementById("barra").value = "";
    id=id - 1
  }
  
  
}

function borrarTag(id){
  document.getElementById(id).remove()
}

                                                                                                                            