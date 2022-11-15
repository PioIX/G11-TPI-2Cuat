src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"

id=0

function Busqueda(){
  tags = document.getElementById("barra").value;
  
  id = id+1
  if(id < 6){
      if(tags.length >= 2){
      document.getElementById("barra").value = "";
        x = id
      document.getElementById("tags").innerHTML += `
     <button type='button' value='${tags}' class="but" id=${id} onclick='borrarTag("${x}" )'>${tags} ✖️</button>
    `
      compararBusqueda(tags,x)
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
  let vector = document.getElementsByName(id)
  
  while (vector.length > 0) {
    vector[0].remove()
    conteo = conteo - 1
  }
  
}

function cargarOptions(){
  opciones = []
  $.ajax({
    url:"/options",
    type:"GET",
    success:function(response){
      datos =  response;
      for(i=0;i<=datos.length ;i++){
        document.getElementById("barra").innerHTML += `
        <option value="${datos[i]}">${datos[i]}</option>
        `
      }
      
    },
  error:function(error){
      console.log(error);
    },
  }); 
} 
  


cargarOptions()
                                                                          