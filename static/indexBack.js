id=0

function Busqueda(){
  tags = document.getElementById("barra").value;
  id = id+1
  if(id < 6){
      if(tags.length >= 2){
      document.getElementById("barra").value = "";
      document.getElementById("tags").innerHTML += `
     <button value='${tags}' class="but" id=${id} onlclick='borrarTag(${id})'>${tags} ✖️</button>
    `
      console.log(tags)
    }else{
      console.log("debe tener almenos 2 letras")
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
  document.getElementBy(id).remove()
  
}

                                                                                                                            