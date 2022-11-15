function recopilarInfo(tags,id){
  console.log(tags)
  compararBusqueda(tags,id)
}

conteo = 0
yaExisten = []
noCumple = []

function compararBusqueda(tags,id) {
  if(conteo >= 1){
    $.ajax({
    url:"/comparar",
    type:"POST",
    data:{"tags":tags,
          "conteo":conteo,
          "yaExisten":yaExisten,
          "noCumple":noCumple
         },
    success:function(response){
      datos =  response;
      if(datos.length>=2){
        for(i=0;i<datos.length;i++){
          if(datos[i] in yaExisten){
            console.log("ya existe")
          }else{
            document.getElementById("box").innerHTML += `
  <buttom type="buttom" class="recetas" onclick="mostrarReceta('${datos[i]}')" name=${id}>${datos[i]}</buttom> 
     `
    yaExisten.push(datos[i])
    conteo = conteo + 1
    console.log("conteo: " + conteo)
    console.log("Lista yaExisten :" + yaExisten)
          }
          
        }
        
    }else{
        document.getElementById("box").innerHTML += `
  <buttom type="buttom" class="recetas" onclick="mostrarReceta('${datos[0]}')" name=${id}>${datos[0]}</buttom> 
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
      if (datos != true){
        if(datos.length>=2){
        for(i=0;i<datos.length;i++){
          document.getElementById("box").innerHTML += `
  <buttom type="buttom" class="recetas" onclick="mostrarReceta('${datos[i]}')" name=${id}>${datos[i]}</buttom> 
     ` 
          yaExisten.push(datos[i])
          console.log("Lista yaExisten: "+ yaExisten)
          conteo = conteo + 1
          console.log("conteo actual: " + conteo)
          
        }
        
    }else{
        document.getElementById("box").innerHTML += `
  <buttom type="buttom" class="recetas" onclick="mostrarReceta('${datos[0]}')" name=${id}>${datos[0]}</buttom> 
     `
        conteo = conteo + document.getElementById("box").children
    }
      }else{
        console.log("ya existe")
      }
      
    },
  error:function(error){
      console.log(error);
    },
  }); 
  }
}


function mostrarReceta(nombre) {

  nombre =  nombre.toLowerCase()
  $.ajax({
    url:"/mostrarReceta",
    type:"POST",
    data:{"nombre":nombre},
    success:function(response){
     datos = (response) 
     console.log("Info receta: ", datos)
     document.getElementById("nombre").innerHTML = `
     <h1>${datos[0][1]}</h1>
     `

      document.getElementById("descripcion").innerHTML = `
     <p>${datos[0][2]}</p>
     `

      document.getElementById("origen").innerHTML = `
     <h3>${datos[0][3]}</h3>
     `
      
    },
    error:function(error){
      console.log(error)
      console.log("NO ANDA :(")
    },
  })


  
}





                                                                        