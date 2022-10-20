import sqlite3
from flask import Flask, render_template,request,session, redirect

app = Flask(__name__)
app.secret_key = 'farandula'


@app.route('/')
def index():
    return render_template('index.html')

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
          return redirect('/')
        else:
          conn.commit()
          conn.close()
          return render_template('/index.html', mostrar = False)
      else:
        redirect('/index')

@app.route('/ingresarReceta', methods = ['POST'])
def ingresarReceta():
  if (request.method['recetaNombre'] != []):
    conn = sqlite3.connect('dataBase.db')
    recetaNombre = request.form['recetaNombre']
    recetaDescripcion = request.form['recetaDescripcion']
    recetaPaisOrigen = request.form['recetaPaisOrigen']
    
    q = f"""INSERT INTO Recetas(nombre, descripcion, pais_origen)
    VALUES({recetaNombre}, {recetaDescripcion}, {recetaPaisOrigen});"""

    conn.execute(q)
    conn.commit()
    conn.close()
@app.route('/buscarReceta', methods = ['GET'])      # busca el nombre
def buscarReceta():    
  return "bottini bot"      #terminar


app.run(host='0.0.0.0', port=81)
