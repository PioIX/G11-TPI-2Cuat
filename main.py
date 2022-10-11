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


app.run(host='0.0.0.0', port=81)
