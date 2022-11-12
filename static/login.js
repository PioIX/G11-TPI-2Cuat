function login(){ // Tendríamos que hacer un login como el de oriana para que cuando el chef ingrese le diga bienvenido y si el usuario chef no eiste entonces que le diga cuenta inexistente o algo por el estilo.
  let login = document.getElementById("login").elements;
  let nombre = login["nombre"].value;
  let contra = login["contra"].value;

  if(/^[a-z0-9]+$/i.test(nombre) == false || /^[a-z0-9]+$/i.test(contra) == false){
    return alert('Deben completarse todos los datos del formulario')
  }else{
    console.log(nombre, contra)
    $.ajax({
      url:"/login", 
      type:"POST",
      data: {nombre:nombre, contra:contra},
      success: function(respuesta){
        if(respuesta == 'True' ){
           window.location = "https://memotest.orianatoscano.repl.co/juego";  
            alert('bienvenide ' + nombre)
        }else{
            alert(respuesta)
        }
      },
      error: function(error){
        console.log(error);
    }, });
  }
};