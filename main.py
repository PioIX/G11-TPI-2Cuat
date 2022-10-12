import sqlite3
from flask import Flask, render_template,request,session

app = Flask(__name__)


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

@app.route('/politicas')
def politicas():
  return render_template('politicas.html')

@app.route('/loginChef', methods = ['GET', 'POST'])
def loginChef():
  if (request.method == 'POST'):
    if (request.mothod['nombre'] != []):
      conn = sqlite3.connect('dataBase.db')
      nombre = request.form['nombre']
      contra = request.form['password']
      
      q = f"""SELECT usuario FROM Chef WHERE nombre = {nombre} and password = '{contra}' ;"""  
      conn.execute(q)
      conn.commit()
      conn.close()



app.run(host='0.0.0.0', port=81)
