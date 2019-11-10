from flask import Flask, render_template, request
import flask
from flask_restful import Api, Resource
import json
from pprint import pprint as print



def add_tarefa(tarefa):
	t = tarefa.tempo
	d = tarefa.dificuldade
	dic = {"tempo": t, "dificuldade": d}
	if dictglobal == {}:
		id_adicionado = 0
	else:
		id_adicionado = (list(dictglobal.keys())[-1])+1
	d = {id_adicionado : dic}
	dictglobal.update(d)
	return id_adicionado

def update_tarefa(tarefa, id_tarefa):
	t = tarefa.tempo
	d = tarefa.dificuldade
	dic = {"tempo": t, "dificuldade": d}
	if dictglobal == {}:
		id_adicionado = 0
	else:
		id_adicionado = (list(dictglobal.keys())[id_tarefa])
	d = {id_adicionado : dic}
	dictglobal.update(d)
	return id_adicionado


def remove_tarefa(id_tarefa):
	del dictglobal[id_tarefa]


# • Crie uma classe denominada Tarefas. Defina pelo menos uns 2 atributos.

class Tarefas():
	def __init__(self, tempo=0, dificuldade=0):
		self.tempo = tempo
		self.dificuldade = dificuldade



#   •   Crie um dicionário global no programa que irá acomodar as tarefas. Defina que a “chave primária” seria
# 		um id autoincremental de tarefas.


dictglobal = {}



# • Crie um webserver em Python usando o Flask.

app = flask.Flask('your_flask_env')



# • Defina 6 endpoints para expor no Flask (trocando informações via JSON):

# – /Tarefa/ - GET: lista todas as tarefas do dicionário.
# – /Tarefa/ - POST: Adiciona uma tarefa.

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
	if flask.request.method == 'POST':
		# adiciona uma tarefa
		add_tarefa(Tarefas(request.get_json()['tempo'], request.get_json()['dificuldade']))
		return ("ok", 200)
	else:
		# lista todas as tarefas do dicionario
		if dictglobal != {}:
			return(str(dictglobal), 200)
		else:
			return("dict vazio", 400)



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
		return """O tempo estimado para a tarefa {0} é de {1} hora(s), e sua dificuldade foi avaliada como {2}; """.format(id_task, dictglobal[id_task]['tempo'], dictglobal[id_task]['dificuldade'])#render_template("index.html")#.format(dictglobal[numero])


# – /healthcheck/ - Retorna o código 200 sem texto.

@app.route('/healthcheck')
def healthy():
	return ("", 200)


# • Teste o serviço acima em localhost, olhando como o dicionário é alterado. Atenção na hora em que serializar
# um objeto da sua classe para o formato


if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=5000)

