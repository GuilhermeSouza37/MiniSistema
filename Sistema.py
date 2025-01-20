
from Menu.Projeto.arquivo.arquivo import *
from Menu.Projeto.interface.interface import *
from time import sleep

cabeçalho('Sistema de Registro')

arq = 'Cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Pessoas Cadastradas')
        lerArquivo(arq)
        # Opção de listar o conteúdo de um arquivo!
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        # Opção de cadastrar uma nova
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')

    sleep(2)


