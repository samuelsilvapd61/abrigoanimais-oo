from auxiliar.texto import Texto
from model.abrigo import Abrigo

lista_abrigos = list()

Texto.titulo('Sistema AbrigoPets!')

while True:
    tarefa = Texto.menu_opcoes(
        '1 - Cadastrar Abrigo',
        '2 - Exibir Abrigos',
        '3 - Apagar Abrigo',
        '4 - Cadastrar Pet',
        '5 - Exibir Pets',
        '6 - Apagar Pet',
        '7 - Sair do Sistema')

    if tarefa == 1:
        # Cadastra o abrigo
        lista_abrigos.append(Abrigo.cadastrar_abrigo(lista_abrigos))

    elif tarefa == 2:
        # Exibe todos os abrigos
        Abrigo.exibir_abrigos(lista_abrigos)

    elif tarefa == 3:
        # Apaga o abrigo
        pass

    elif tarefa == 4:
        # Cadastra o pet
        pass

    elif tarefa == 5:
        # Exibe todos os pets de um determinado abrigo
        pass

    elif tarefa == 6:
        # Apaga o pet
        pass

    elif tarefa == 7:
        # Sai do loop e deixa o programa finalizar naturalmente.
        print('Finalizando o Sistema...')
        break
    print()
    Texto.linha()


