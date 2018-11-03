from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template , request, url_for, redirect
from flask_mail import Mail, Message
from flask import session
from config import DevelopmentConfig
import os

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


mail= Mail(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'proyecto'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
mysql.init_app(app)


@app.route('/')
def index():
	
	return render_template('main.html') #regresa string

@app.route('/inicio')
def inicio():
	
	return render_template('index.html') #regresa string


@app.route('/iniciarsesion')#decorador unica ruta donde el usuario puede entrar
def iniciarSesion():
	
		return render_template('iniciarsesion.html')

@app.route('/login', methods=['POST'])#decorador unica ruta donde el usuario puede entrar
def login():
		if request.method == 'POST':
		  nombre = str(request.form['nombre'])
		  clave = str(request.form['pass'])
		  conn = mysql.connect()
		  cursor = conn.cursor()
		  cursor.execute("SELECT nombre FROM usuario WHERE nombre ='"+nombre+"' and clave = '"+clave+"' ")
		  usuario = cursor.fetchone()
		 
		  if usuario is None or len(usuario) ==0:
			return "failed"
		  else:
			return render_template('index.html')


@app.route('/crear_oa')#decorador unica ruta donde el usuario puede entrar
def crear_oa():
	
		return render_template('crear_oa.html')

@app.route('/perfil')#decorador unica ruta donde el usuario puede entrar
def perfil():
	
		return render_template('perfil.html')

@app.route('/registro2', methods=['POST'])#decorador unica ruta donde el usuario puede entrar
def registro2():
		if request.method == 'POST':
		  nombre = request.form['nombre']
		  apellido = request.form['apellido']
		  carrera = request.form['carrera']
		  email = request.form['email']
		  clave = request.form['pass']
		  sexo = request.form['sexo']
		  print(nombre)
		  conn = mysql.connect()
		  cursor = conn.cursor()
		  cursor.execute( 'INSERT INTO usuario (nombre,apellido,carrera,email,clave,sexo,tipousuario_idtipousuario,estado) VALUES (%s,%s,%s,%s,%s,%s,2,0)',(nombre,apellido,carrera,email,clave,sexo))
		  conn.commit()
		  msg= Message('Gracias por tu registro',
		  	sender = app.config['MAIL_USERNAME'],
		  	recipients =[email])
		  msg.html = render_template('correoRegistro.html')
		  mail.send(msg)
		  return render_template('registroexitoso.html')


@app.route('/registro')
def registro():
	return render_template('registro.html')

@app.route('/sugerencias')
def sugerencias():
	return render_template('sugerencias.html')

@app.route('/admin')
def admin():
	return render_template('administrador.html')

@app.route('/pass')
def password():
	return render_template('cambiarPass.html')

@app.route('/crearOa')
def crear():
	return render_template('crear_oa.html')

@app.route('/reportar')
def reportar():
	return render_template('reportar_oa.html')

@app.route('/registroexitoso')
def registro3():
	return render_template('registroexitoso.html')

if __name__ == '__main__':
  app.run(port=8000)
  