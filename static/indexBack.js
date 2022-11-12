function recopilarInfo(tags,id){
  console.log(tags)
  compararBusqueda(tags,id)
}

conteo = 0
yaExisten = []

function compararBusqueda(tags,id) {
  if(conteo >= 1){
    $.ajax({
    url:"/comparar",
    type:"POST",
    data:{"tags":tags,
          "conteo":conteo},
    success:function(response){
      datos =  response;
      console.log(datos)
      if(datos.length>=2){
        for(i=0;i<datos.length;i++){
          if(datos[i] in yaExisten){
            console.log("ya existe")
          }else{
            document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[i]}</buttom> 
  `
    yaExisten.push(datos[i])
    conteo = conteo + document.getElementById("box").children.length
          }
          
        }
        
    }else{
        document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[0]}</buttom> 
     `
        conteo = conteo + document.getElementById("box").children
    }
    },
  error:function(error){
      console.log(error);
    },
  }); 
  }else{
   $.ajax({
    url:"/comparar",
    type:"POST",
    data:{"tags":tags,
          "conteo":conteo},
    success:function(response){
      datos =  response;
      console.log(datos)
      if(datos.length>=2){
        for(i=0;i<datos.length;i++){
          document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[i]}</buttom> 
  `
    conteo = conteo + document.getElementById("box").children.length
        }
        
    }else{
        document.getElementById("box").innerHTML += `
  <buttom class="recetas" name=${id}>${datos[0]}</buttom> 
     `
        conteo = conteo + document.getElementById("box").children
    }
    },
  error:function(error){
      console.log(error);
    },
  }); 
  }
}






                                                                        