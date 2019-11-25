from flask import Flask, render_template, request
import flask
from flask_restful import Api, Resource
import json
import pymongo
import os

ipBD = os.environ['ipBD']

client = pymongo.MongoClient("mongodb://sabrina:mongolito@{0}/tarefas".format(ipBD)) # defaults to port 27017

db = client.tarefas

tarefas = db.tarefas

dictglobal = {}
global id_adicionado
id_adicionado = 0
def add_tarefa(tarefa, idee):
	t = tarefa.tempo
	d = tarefa.dificuldade
	dic = {"tempo": t, "dificuldade": d}
	mydict = {"_id" : idee, "tempo": t, "dificuldade": d}
	tarefas.insert_one(mydict)
	return idee

def update_tarefa(tarefa, id_tarefa):
	t = tarefa.tempo
	d = tarefa.dificuldade
	dic = {"tempo": t, "dificuldade": d}
	if dictglobal == {}:
		id_adicionado = 0
	else:
		id_adicionado = (list(dictglobal.keys())[id_tarefa])
	myquery = { "_id": id_tarefa }
	newvalues = { "$set": dic }

	tarefas.update_one(myquery, newvalues)
	return id_adicionado

def remove_tarefa(id_tarefa):
	myquery = { "_id": id_tarefa }

	tarefas.delete_one(myquery)


# • Crie uma classe denominada Tarefas. Defina pelo menos uns 2 atributos.

class Tarefas():
	def __init__(self, tempo=0, dificuldade=0):
		self.tempo = tempo
		self.dificuldade = dificuldade



#   •   Crie um dicionário global no programa que irá acomodar as tarefas. Defina que a “chave primária” seria
# 		um id autoincremental de tarefas.




# • Crie um webserver em Python usando o Flask.

app = flask.Flask('your_flask_env')



# • Defina 6 endpoints para expor no Flask (trocando informações via JSON):

# – /Tarefa/ - GET: lista todas as tarefas do dicionário.
# – /Tarefa/ - POST: Adiciona uma tarefa.

@app.route('/Tarefa', methods=['GET', 'POST'])
# @app.route("/<path:path>")
def Tarefa():
	global id_adicionado
	id_adicionado = 0
	if flask.request.method == 'POST':
		# adiciona uma tarefa
		vai = []
		if db.tarefas.find() != []:
			for x in db.tarefas.find().sort("_id",-1):
				vai.append(x)
				break
			iii = int(vai[0]['_id']) + 1
		else:
			iii = 0
		add_tarefa(Tarefas(request.get_json()['tempo'], request.get_json()['dificuldade']), iii)
		id_adicionado += 1
		return ("ok", 200)
	else:
		# lista todas as tarefas do dicionario
		vai = []
		for x in tarefas.find():
			vai.append(x)
		return(str(vai), 200)



# – /Tarefa/<id> - GET: lista a tarefa com o determinado id.
# – /Tarefa/<id> - PUT: atualiza uma tarefa com o determinado id.
# – /Tarefa/<id> - DELETE: apaga a tarefa com o determinado id.

@app.route('/Tarefa/<int:id_task>', methods=['GET', 'PUT', 'DELETE'])
def TarefaID(id_task):
	if flask.request.method == 'DELETE':
		remove_tarefa(id_task)
		return ("ok", 200)
	elif flask.request.method == 'PUT':
		print(request.get_json())
		update_tarefa(Tarefas(request.get_json()['tempo'], request.get_json()['dificuldade']), id_task)
		return ("ok", 200) #dictglobal[numero]
	else:
		vai = []
		for x in tarefas.find({ "_id": id_task}):
			vai.append(x)
		return(str(vai), 200)#render_template("index.html")#.format(dictglobal[numero])


# – /healthcheck/ - Retorna o código 200 sem texto.

@app.route('/healthcheck')
def healthy():
	return ("", 200)



# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path, methods=['GET', 'PUT', 'DELETE', 'POST']):
# 	if flask.request.method == 'DELETE':
# 		remove_tarefa(id_task)
# 		return ("ok", 200)
# 	elif flask.request.method == 'PUT':
# 		print(request.get_json())
# 		update_tarefa(Tarefas(request.get_json()['tempo'], request.get_json()['dificuldade']), id_task)
# 	elif flask.request.method == 'POST':
# 		add_tarefa(Tarefas(request.get_json()['tempo'], request.get_json()['dificuldade']))
# 		return ("ok", 200)
# 	elif flask.request.method == 'GET':
# 		if dictglobal != {}:
# 			return(str(dictglobal), 200)
# 		else:
# 			return("dict vazio", 400)
# 	else:
#     	return 'You want path: %s' % path


# • Teste o serviço acima em localhost, olhando como o dicionário é alterado. Atenção na hora em que serializar
# um objeto da sua classe para o formato


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)

