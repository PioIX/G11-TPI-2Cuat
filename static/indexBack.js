function recopilarInfo(tags,id){
  console.log(tags)
  compararBusqueda(tags,id)
}

function compararBusqueda(tags,id) {
  $.ajax({
    url:"/comparar",
    type:"POST",
    data:{"tags":tags},
    success:function(response){
      datos =  response;
      console.log(datos)
      if(datos.length>=2){
        for(i=0;i<datos.length;i++){
          document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[i]}</buttom> 
  `
  
        }
        
    }else{
        document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[0]}</buttom> 
     `
    }
    },
  error:function(error){
      console.log(error);
    },
  });
}






                                                                          