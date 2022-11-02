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
      document.getElementById("box").innerHTML += `
  <h1 id=${id}>${datos}</h1>
  `
    },
    error:function(error){
      console.log(error);
    },
  });
}






                                                                          