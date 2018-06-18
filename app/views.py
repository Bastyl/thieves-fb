from app import app
from flask import render_template
from flask import request
from app.configuraciones import *


import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
@app.route('/index',methods=['POST','GET'])
def index():

	sql = """SELECT * FROM delincuentes;"""
	cur.execute(sql)
	datos = cur.fetchall()

	sql = """SELECT * FROM caracteristicas;"""
	cur.execute(sql)
	apariencia = cur.fetchall()

	sql = """SELECT * FROM historial;"""
	cur.execute(sql)
	historial = cur.fetchall()

	return render_template("index.html",datos=datos,apariencia=apariencia,historial=historial)


@app.route('/buscar',methods=['GET'])
def buscar_delincuente():
	if request.method == 'GET' and request.args.get('sexo') != None:
		sexo = request.args.get('sexo')
		sql = """SELECT delincuentes FROM delincuentes,caracteristicas WHERE sexo = '%s' AND delincuentes.id = caracteristicas.usuario_id;"""%(sexo)
		cur.execute(sql)
		sospechosos = cur.fetchall()
		return lista(sospechosos)
	return render_template("buscar_delincuente.html")

#retorna la lista con los posibles sospechosos, falta agregar boton al lado de cada nombre para redireccionar a "delincuente"

def lista(sospechosos):
	return render_template("lista.html",sospechosos=sospechosos)

@app.route('/delincuente/<id>',methods=['GET','POST'])
def delincuente(id):
	sql = """SELECT delincuentes,historial FROM delincuentes,historial WHERE delincuentes.id = historial.usuario_id AND delincuentes.id = '%s';"""%(id)
	cur.execute(sql)
	datos = cur.fetchall()
	if request.method == 'POST':
		historia = request.form['historia']
		print(historia)
		sql = """INSERT INTO historial (usuario_id,sector,relato,fecha,hora) values (('%s'), ('%s'), ('%s'), ('%s'),('%s'));"""%(id,"puentealto",historia,123,413)
		cur.execute(sql)
		conn.commit()

		sql = """SELECT delincuentes,historial FROM delincuentes,historial WHERE delincuentes.id = historial.usuario_id AND delincuentes.id = '%s';"""%(id)
		cur.execute(sql)
		datos = cur.fetchall()

	return render_template("delincuente.html",datos=datos)
