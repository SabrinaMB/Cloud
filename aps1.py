from flask import Flask, render_template
import flask
from flask_restful import Api, Resource
import json

# • Crie uma classe denominada Tarefas. Defina pelo menos uns 2 atributos.

class Tarefas():
	atributo1 = "lala"
	atributo2 = "qqqq"

#   •   Crie um dicionário global no programa que irá acomodar as tarefas. Defina que a “chave primária” seria
# 	    um id autoincremental de tarefas.
print(Tarefas)
dictglobal = {}

listaTarefas = ["tarefa1", "tarefa2"]

pk = 0

for tarefa in listaTarefas:
    pk += 1
    dictglobal [pk] = tarefa

def add_tarefa(tarefa):
	id_adicionado = list(dictglobal.keys())[-1]+1
	d = {id_adicionado : tarefa}
	dictglobal.update(d)
	return id_adicionado

def remove_tarefa(id_tarefa):
    del dictglobal[id_tarefa]

add_tarefa("hellooo")
add_tarefa("?????")
add_tarefa("yay!!!")
print (dictglobal[2])

# • Crie um webserver em Python usando o Flask.

app = flask.Flask('your_flask_env')

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    if flask.request.method == 'POST':
    	# adiciona uma tarefa
        # username = flask.request.values.get('user') # Your form's
        # password = flask.request.values.get('pass') # input names
        # your_register_routine(username, password)
        pass
    else:
    	# lista todas as tarefas do dicionario

        # You probably don't have args at this route with GET
        # method, but if you do, you can access them like so:
        # yourarg = flask.request.args.get('argname')
        # your_register_template_rendering(yourarg)
        return str(dictglobal)

@app.route('/Tarefa/<id_task>', methods=['GET', 'PUT', 'DELETE'])
def TarefaID(id_task):
    if flask.request.method == 'DELETE':
    	remove_tarefa(id_task)
    	return
    elif flask.request.method == 'PUT':
    	if "Do Something" in request.form:
    		tarefa = flask.request.form('tarefa')
    		numero = add_tarefa(tarefa)
    	return request.form #dictglobal[numero]
    else:
        numero = int(id_task)
    return render_template("index.html")#.format(dictglobal[numero])
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# • Defina 6 endpoints para expor no Flask (trocando informações via JSON):
# – /Tarefa/ - GET: lista todas as tarefas do dicionário.
# – /Tarefa/ - POST: Adiciona uma tarefa.
# – /Tarefa/<id> - GET: lista a tarefa com o determinado id.
# – /Tarefa/<id> - PUT: atualiza uma tarefa com o determinado id.
# – /Tarefa/<id> - DELETE: apaga a tarefa com o determinado id.
# – /healthcheck/ - Retorna o código 200 sem texto.
# • Teste o serviço acima em localhost, olhando como o dicionário é alterado. Atenção na hora em que serializar
# um objeto da sua classe para o formato



app = Flask(__name__)
api = Api(app)




class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')


