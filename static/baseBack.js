
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
      recopilarInfo(tags,x)
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
  document.getElementById(id).remove() 
}
/*
$(function()
	{
		var mySelectCheckbox = new checkbox_select(
		{
			selector : "#make_checkbox_select",
            selected_translation : "selectat",
            all_translation : "Toate marcile",
            not_found : "Nici unul gasit",

			// Event during initialization
			onApply : function(e)
			{
                alert("Custom Event: " + e.selected);
			}
		});
  
	});
*/

                                                                          