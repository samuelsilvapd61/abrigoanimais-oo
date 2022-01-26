from auxiliar.texto import Texto

Texto.titulo('Sistema AbrigoPets!')

while True:
    tarefa = Texto.menu_opcoes(
        '1 - Cadastrar Abrigo',
        '2 - Cadastrar Pet',
        '3 - Apagar Abrigo',
        '4 - Apagar Pet',
        '5 - Sair do Sistema')

    if tarefa == 1:
        print('Cadastrar Abrigo...')
    elif tarefa == 2:
        print('Cadastrar Pet...')
    elif tarefa == 3:
        print('Apagar Abrigo...')
    elif tarefa == 4:
        print('Apagar Pet...')
    elif tarefa == 5:
        print('Finalizando o Sistema...')
        break
    Texto.linha()


