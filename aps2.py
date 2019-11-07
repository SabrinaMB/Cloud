import os

#  Inicie o servidor feito no APS anterior.
# • Crie um script que cria uma variável de ambiente com o endereço do servidor.

# • Escreva um programa tarefa.py que recebe argumentos de entrada (sys.argv) com as seguintes ações:


# – $ tarefa adicionar [lista de valores dos atributos da classe]
# – $ tarefa listar
# – $ tarefa buscar
# – $ tarefa apagar
# – $ tarefa atualizar [lista de valores dos atributos da classe]
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
os.putenv("EnderecoServidor", "http://localhost:5000")
print(os.environ)