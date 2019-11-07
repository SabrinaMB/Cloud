import os
import sys
from aps1 import *
import requests 
#!/usr/bin/env python3

#  Inicie o servidor feito no APS anterior.
# • Crie um script que cria uma variável de ambiente com o endereço do servidor.

# • Escreva um programa tarefa.py que recebe argumentos de entrada (sys.argv) com as seguintes ações:

# – $ tarefa adicionar [lista de valores dos atributos da classe]


class Tarefas():
	def __init__(self, tempo=0, dificuldade=0):
		self.tempo = tempo
		self.dificuldade = dificuldade


URLbase = os.environ['EnderecoServidor']
print(URLbase)
# – $ tarefa listar
# – $ tarefa buscar
# – $ tarefa apagar
# – $ tarefa atualizar [lista de valores dos atributos da classe]

acao = sys.argv[1]
if len(sys.argv) >= 3:

	id_tarefa = int(sys.argv[2])
if len(sys.argv) == 4:
	tempo = int(sys.argv[2])
	dificuldade = int(sys.argv[3])
if len(sys.argv) == 5:
	tempo = int(sys.argv[2])
	dificuldade = int(sys.argv[3])
	id_tarefa = int(sys.argv[4])


# defining a params dict for the parameters to be sent to the API 
PARAMS = {"tempo" : 0, "dificuldade" : 0} 
  


#Tarefas
if acao == "adicionar":
	print("adicionar")
	URL = URLbase + "/Tarefa"
	r = requests.post(url = URL, json = PARAMS) 
	print(r)

elif acao == "listar":
	print("listar")
	URL = URLbase + "/Tarefa"
	r = requests.get(url = URL, json = PARAMS) 
	print(r)

#TarefaID
elif acao == "buscar":
	print("buscar")
	URL = URLbase + "/Tarefa/{0}".format(id_tarefa)
	r = requests.get(url = URL, json = PARAMS) 
	print(r)
	
elif acao == "apagar":
	print("apagar")
	URL = URLbase + "/Tarefa/{0}".format(id_tarefa)
	r = requests.delete(url = URL, json = PARAMS) 
	print(r)

elif acao == "atualizar":
	print("atualizar")
	URL = URLbase + "/Tarefa/{0}".format(id_tarefa)
	r = requests.put(url = URL, json = PARAMS) 
	print(r)

else:
	pass

# print(data)
print("uhull!!! " + str(acao))


# • O comandos acima são equivalentes aos endpoints expostos no APS anterior.
# • Utilize a biblioteca requests para realizar as requisições, tratando o JSON correspondente.
# • Modifique o nome do arquivo para tarefa apenas.
# • Adicione o cabeçalho: #!/usr/bin/env python3.
# • Dê permissão de execução para o script.
# • Coloque-o no path.
# • teste novamente, chamando-o diretamente: $ tarefa listar
# • Escreva um help com carinho.
# • Envie o código para o seu GitHub.

# os.environ('export ENDSER="http://localhost:5000"')
# dic = os.environ
# ndic = {"EnderecoServidor" : "http://localhost:5000"}
# dic.update(ndic)
# os.putenv("EnderecoServidor", "http://localhost:5000")
# print(os.environ)