from auxiliar.texto import Texto


class Abrigo:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.endereco = ''
        self.animais = dict()

    # Usuário informa ID do abrigo.
    # Se o ID do abrigo não existir, o usuário informa nome e endereço do abrigo.
    @staticmethod
    def cadastrar_abrigo(lista):
        abrigo = Abrigo()
        id = int(input('Digite o ID do Abrigo: '))

        id_existe = Abrigo.abrigo_existe(id, lista)
        if not id_existe:
            abrigo.id = id
            abrigo.nome = input('Digite o nome do Abrigo: ')
            abrigo.endereco = input('Digite o endereço do Abrigo: ')

        print(f'Abrigo {abrigo.nome} cadastrado com sucesso!')

        return abrigo

    # Lista as informações de todos os abrigos.
    # Não lista os pets.
    @staticmethod
    def exibir_abrigos(lista):
        for abrigo in lista:
            Abrigo.exibir_abrigo(abrigo)

    # Usuário informa o ID do abrigo.
    # Se o ID existir, o abrigo é deletado.
    def apagar_abrigo(self):
        pass

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o usuário informa o ID do pet.
    # Se o ID do pet não existir, então o usuário informa o nome do pet.
    def cadastrar_pet(self):
        pass

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o programa lista os pets desse abrigo.
    def exibir_pets(self):
        pass

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o usuário informa o ID do pet.
    # Se o ID do pet existir, então o pet é deletado.
    def apagar_pet(self):
        pass

    # Verifica a existência do ID do abrigo e retorna um booleano
    @staticmethod
    def abrigo_existe(id, lista):
        id_existe = False
        for abrigo in lista:
            if id == abrigo.id:
                id_existe = True
                break

        return id_existe

    # Exibe as informações do abrigo em questão
    @staticmethod
    def exibir_abrigo(abrigo):
        print(f'ID: {abrigo.id} - Nome: {abrigo.nome} - Endereço: {abrigo.endereco}')


