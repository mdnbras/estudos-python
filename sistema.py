from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'db.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Sair do sistema'
    ])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        cadastrarPessoa(arq, str(input('Nome: ')), leiaInt('Idade: '))
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
    sleep(1)
