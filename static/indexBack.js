function recopilarInfo(tags,id){
  console.log(tags)
  document.getElementById("box").innerHTML += `
  <h1 id=${id}>${tags}</h1>
  `
}

function compararBusqueda(tags) {
  $.ajax({
    url:"...",
    type:"POST",
    data:{"tags":tags},
    success:function(response){
      datos = JSON.parse(response);
    },
    error:function(error){
      console.log(error);
    },
  });
}






                                                                          