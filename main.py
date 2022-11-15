import sqlite3
from flask import Flask, render_template,request,session, redirect,jsonify

app = Flask(__name__)
app.secret_key = 'farandula'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indexChef')
def indexChef():
    return render_template('indexChef.html')

@app.route('/modificar')
def modificar():
    return render_template('modificar.html')

@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/eliminar')
def eliminar():
    return render_template('eliminar.html')

@app.route('/options')
def cargarOptions():
  if(request.method == "GET"):
    
    conn = sqlite3.connect('dataBase.db')
    cur = f""" SELECT nombre FROM Ingredientes;"""
    resultado = conn.execute(cur)
    opciones = resultado.fetchall()
    return jsonify(opciones)





@app.route('/comparar', methods = ['POST'])
def comparacion():
  if (request.method == "POST"):

    #obtengo informacion
    busqueda = request.form["tags"]
    print(busqueda)
    conteo = request.form["conteo"]
    busqueda = busqueda.lower()
    print(conteo)

    #me fijo si hay ya recetas mostradas
    if (int(conteo) >= 1):

      #busco en la base de datos las recetas que tengan el ingrediente
      yaExisten = request.form["yaExisten"]
      conn = sqlite3.connect('dataBase.db')
      cur = f"""SELECT id_ingrediente FROM Ingredientes      WHERE nombre == '{busqueda}';"""
                    
      resultado = conn.execute(cur)
      dato = resultado.fetchone()
  
      resu = f""" SELECT Lista_ingredientes.id_receta FROM Lista_ingredientes INNER JOIN Ingredientes ON Lista_ingredientes.id_ingrediente = Ingredientes.id_ingrediente WHERE Ingredientes.id_ingrediente = {dato[0]};"""
      
      rese = conn.execute(resu)
      rese = rese.fetchall()
      lista = []
      i=0

      
      if(len(rese) >= 2):

        
          for i in range(len(rese)):
            messi = f""" SELECT nombre FROM Recetas WHERE id_receta == {rese[i][0]};"""
            mesi = conn.execute(messi)
            mesi = mesi.fetchone()
            lista.append(mesi)
            i = i +1
          
          conn.close()
        
          for i in range(len(lista)):

            #me fijo si las recetas ya estan mostradas en la pagina
            if(lista[i] in yaExisten):
              
              lista.remove(lista[i])
              i = i +1
            else:
              i = i +1
      
          return jsonify(lista)
        
      else:
        
        messi = f""" SELECT nombre FROM Recetas WHERE id_receta == {rese[0][0]};"""
        mesi = conn.execute(messi)
        mesi = mesi.fetchone()
        conn.close()
        if messi in yaExisten:
          print("ya existe")
          return True
          
    else:
      conn = sqlite3.connect('dataBase.db')
      cur = f"""SELECT id_ingrediente FROM Ingredientes  WHERE nombre == '{busqueda}';"""
                    
      resultado = conn.execute(cur)
      dato = resultado.fetchone()
  
      resu = f""" SELECT Lista_ingredientes.id_receta FROM Lista_ingredientes INNER JOIN Ingredientes ON Lista_ingredientes.id_ingrediente = Ingredientes.id_ingrediente WHERE Ingredientes.id_ingrediente = {dato[0]};"""
      
      rese = conn.execute(resu)
      rese = rese.fetchall()
      lista = []
      i=0
      
      if(len(rese) >= 2):
          for i in range(len(rese)):
            messi = f""" SELECT nombre FROM Recetas WHERE id_receta == {rese[i][0]};"""
            mesi = conn.execute(messi)
            mesi = mesi.fetchone()
            lista.append(mesi)
            i = i +1
          conn.close()
          return jsonify(lista) 
        
      else:
        
        messi = f""" SELECT nombre FROM Recetas WHERE id_receta == {rese[0][0]};"""
        mesi = conn.execute(messi)
        mesi = mesi.fetchone()
        conn.close()
        return jsonify(mesi) 





@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/ayuda')
def ayuda():
  return render_template('ayuda.html')

@app.route('/nosotros')
def nosotros():
  return render_template('nosotros.html')

@app.route('/opinion')
def opinion():
  return render_template('opinion.html')



@app.route('/loginChef', methods = ['GET', 'POST'])
def loginChef():
    if (request.method == 'POST'):
      if (request.form['nombre'] != ""):
        conn = sqlite3.connect('dataBase.db')
        nombre = request.form['nombre']
        contra = request.form['password']
        
        q = f"""SELECT usuario FROM Chefs WHERE usuario = '{nombre}' and contra = '{contra}' ;"""  
        resu = conn.execute(q)

        if resu.fetchone():
          conn.commit()
          conn.close()
          return redirect('/indexChef') 
          # preguntar como seria un reedirect con una variable incluida (algo como lo de abajo)
        else:
          conn.commit()
          conn.close()
          return render_template('/index.html', mostrar = False)    # (lo de arriba se refiere al "mostrar" de esta linea)
      else:
        redirect('/index')




@app.route('/ingresarReceta', methods = ['POST'])
def ingresarReceta():

  
  if (request.method['recetaNombre'] != ''):
    conn = sqlite3.connect('dataBase.db')
    recetaNombre = request.form['recetaNombre']
    recetaDescripcion = request.form['recetaDescripcion']
    recetaPaisOrigen = request.form['recetaPaisOrigen']
    
    q = f"""INSERT INTO Recetas(nombre, descripcion, pais_origen)
    VALUES({recetaNombre}, {recetaDescripcion}, {recetaPaisOrigen});"""    # chequear que esto funcione

    conn.execute(q)
    conn.commit()
    conn.close()
     

    

@app.route('/visualizarRecetas', methods = ['POST'])
def visualizarRecetas():
  conn = sqlite3.connect('dataBase.db')
  q = """SELECT nombre FROM Recetas;"""
  conn.execute(q)
  print(q)


def checkearSiExiste(unNombre):  # es para los ingedientes
    conn = sqlite3.connect('dataBase.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT nombre FROM Ingredientes WHERE nombre = '{unNombre}';""")
    resu = cur.fetchall()
    conn.commit()
    conn.close()
    if resu != []:
      return True

@app.route('/nIngrediente', methods = ['GET', 'POST'])    # crear el formulario - cumplir con el argumento 'nombre'
def nIngediente():
  if (request.method == 'POST'):
    nombre = request.form['nombre']
    if (checkearSiExiste(nombre) == False):
      nombre = request.form['nombre']
      conn = sqlite3.connect('dataBase.db')
      q = f"""INSERT INTO Ingredientes(nombre)
    VALUES({nombre};"""
      conn.execute(q)
      conn.commit()
      conn.close()
      print('ejecutado, ', nombre)


@app.route('/mostrarReceta', methods = ['GET', 'POST'])
def mostrarRecetas():
  if (request.method == "POST"):
    nombre = request.form['nombre']
    nombre = nombre.lower()
    conn = sqlite3.connect('dataBase.db')
    print(nombre)
    q = f"""SELECT id_receta FROM Recetas WHERE nombre LIKE '{nombre}'; """
    q = conn.execute(q)
    id = q.fetchone()
    print(id)
    resu = f"""SELECT * FROM Recetas WHERE id_receta LIKE '{id[0]}'; """
    resu = conn.execute(resu)
    data = resu.fetchall()
    print(data)
    conn.close()
    return jsonify(data)

def checkearSiExiste(id):  # es para las recetas
    conn = sqlite3.connect('dataBase.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT nombre FROM Recetas WHERE Recetas.id = '{id}';""")
    resu = cur.fetchall()
    conn.commit()
    conn.close()
    if resu != []:
      return True

@app.route('/eliminarReceta', methods = ['GET'])
def eliminarReceta(id):
  if (checkearSiExiste(id) == True):
    conn = sqlite3.connect('dataBase.db') 
    q = f"""DELETE FROM Recetas WHERE Recetas.id = {id}; """
    conn.execute(q)
    conn.commit()
    conn.close()
  else: 
    print('el ID ', id, ' no existe')
    

    
# @app.route('/buscarReceta', methods = ['GET', 'POST'])      # busca el nombre
# def buscarReceta():    
#   conn = sqlite3.connect('dataBase')
#   buscada = request.form['buscada']

#   q = f"""SELECT Recetas.nombre FROM Recetas INNER JOIN Chefs ON Recetas.id_chef = Chefs.id_chef WHERE Recetas.nombre LIKE {buscada};"""      # chequear que esto funcione

#   consulta = conn.execute(q)

#   if (consulta == ""):    # arreglar condicion (si "q" no resulta ver lo que devuelve, ¿NULL, 0?)
#     pass

# # hay que hacer que 
    
# #para la siguiente hay que hacer que se pasen los datos de la receta seleccionada entre el apartado de los filtros y la vista de la receta

app.run(host='0.0.0.0', port=81)
