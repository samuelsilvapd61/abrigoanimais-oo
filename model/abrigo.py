from auxiliar.texto import Texto
from model.pet import *


class Abrigo:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.endereco = ''
        self.animais = {'Cachorro': [], 'Gato': [], 'Passaro': [], 'Peixe': []}

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
            lista.append(abrigo)

            print(f'Abrigo {abrigo.nome} cadastrado com sucesso!')

        else:
            print(f'O ID {id} já existe, não é possível criar um novo Abrigo com este ID.')

    # Lista as informações de todos os abrigos.
    # Não lista os pets.
    @staticmethod
    def exibir_abrigos(lista):
        Texto.linha()
        for abrigo in lista:
            Abrigo.exibir_abrigo(abrigo)

    # Usuário informa o ID do abrigo.
    # Se o ID existir, o abrigo é deletado.
    @staticmethod
    def apagar_abrigo(lista):
        id = int(input('Digite o ID do Abrigo: '))

        id_existe, abrigo = Abrigo.abrigo_existe(id, lista, True)
        if id_existe:
            lista.remove(abrigo)
            print(f'Abrigo ID: {abrigo.id} - Nome: {abrigo.nome} removido com sucesso!')
        else:
            print(f'ID: {id} inexistente.')

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o usuário informa o ID do pet.
    # Se o ID do pet não existir, então o usuário informa o nome do pet.
    @staticmethod
    def cadastrar_pet(lista):
        # abrigo = Abrigo()
        id_abrigo = int(input('Digite o ID do Abrigo: '))

        id_abrigo_existe, abrigo = Abrigo.abrigo_existe(id_abrigo, lista, True)
        if id_abrigo_existe:
            id_pet = int(input('Digite o ID do pet: '))

            id_pet_existe = Abrigo.pet_existe(id_pet, abrigo.animais)
            if not id_pet_existe:
                opcao = Texto.menu_opcoes('1 - Cachorro', '2 - Gato', '3 - Pássaro', '4 - Peixe')
                pet = None
                while True:
                    if opcao == 1:
                        pet = Cachorro()
                        break
                    elif opcao == 2:
                        pet = Gato()
                        break
                    elif opcao == 3:
                        pet = Passaro()
                        break
                    elif opcao == 4:
                        pet = Peixe()
                        break
                    else:
                        print('Digite uma opção válida!')

                especie = pet.__class__.__name__
                pet.id = id_pet
                pet.nome = input('Digite o nome do pet: ')
                if especie not in abrigo.animais:
                    abrigo.animais[especie] = [pet]
                else:
                    abrigo.animais[especie].append(pet)

                print(f'Pet ID: {pet.id} - Nome: {pet.nome} cadastrado no Abrigo: {abrigo.nome} com sucesso!')

            else:
                print(f'O ID {id_pet} já existe, não é possível criar um novo Pet com este ID.')
        else:
            print(f'ID: {id_abrigo} inexistente.')

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o programa lista os pets desse abrigo.
    @staticmethod
    def exibir_pets(lista):
        id = int(input('Digite o ID do Abrigo: '))

        id_existe, abrigo = Abrigo.abrigo_existe(id, lista, True)
        if id_existe:
            Texto.linha()
            print(f'Lista de Pets do abrigo {abrigo.nome}: ')

            for especie, lista_pets in abrigo.animais.items():
                print(f'{especie}:')
                for pet in lista_pets:
                    print('    ', end='')
                    Abrigo.exibir_pet(pet)

        else:
            print(f'ID: {id} inexistente.')

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o usuário informa o ID do pet.
    # Se o ID do pet existir, então o pet é deletado.
    @staticmethod
    def apagar_pet(lista=[]):
        id_abrigo = int(input('Digite o ID do Abrigo: '))

        id_abrigo_existe, abrigo = Abrigo.abrigo_existe(id_abrigo, lista, True)
        if id_abrigo_existe:
            id_pet = int(input('Digite o ID do pet: '))

            id_pet_existe, pet = Abrigo.pet_existe(id_pet, abrigo.animais, True)
            if id_pet_existe:
                especie = pet.__class__.__name__
                abrigo.animais[especie].remove(pet)

                print(f'Pet ID: {pet.id} - Nome: {pet.nome} do Abrigo: {abrigo.nome} apagado com sucesso!')

            else:
                print(f'ID {id_pet} inexistente.')
        else:
            print(f'ID: {id_abrigo} inexistente.')

    # Usuário informa o ID do abrigo.
    # Se o ID do abrigo existir, o usuário informa o ID do pet.
    # Se o ID do pet existir, o bet brinca.
    @staticmethod
    def bricar_pet(lista):
        id_abrigo = int(input('Digite o ID do Abrigo: '))

        id_abrigo_existe, abrigo = Abrigo.abrigo_existe(id_abrigo, lista, True)
        if id_abrigo_existe:
            id_pet = int(input('Digite o ID do pet: '))

            id_pet_existe, pet = Abrigo.pet_existe(id_pet, abrigo.animais, True)
            if id_pet_existe:
                pet.brincar()

            else:
                print(f'ID {id_pet} inexistente.')
        else:
            print(f'ID: {id_abrigo} inexistente.')

    # Verifica a existência do ID do abrigo e retorna um booleano
    # Se 'retorna_abrigo' = True, então retorna um objeto do tipo Abrigo()
    @staticmethod
    def abrigo_existe(id, lista, retorna_abrigo=False):
        id_existe = False
        abrigo = Abrigo()
        for abrigo in lista:
            if id == abrigo.id:
                id_existe = True
                break

        if retorna_abrigo:
            return id_existe, abrigo
        return id_existe

    # Exibe as informações do abrigo em questão
    @staticmethod
    def exibir_abrigo(abrigo):
        print(f'ID: {abrigo.id} - Nome: {abrigo.nome} - Endereço: {abrigo.endereco}')

    # Verifica a existência do ID do pet e retorna um booleano
    # Se 'retorna_pet' = True, então retorna um objeto do tipo Pet()
    @staticmethod
    def pet_existe(id, dict, retorna_pet=False):
        id_existe = False
        animal = Animal()
        for lista in dict.values():
            for animal in lista:
                if id == animal.id:
                    id_existe = True
                    break
            if id_existe:
                break
        if retorna_pet:
            return id_existe, animal
        return id_existe

    # Exibe as informações do pet em questão
    @staticmethod
    def exibir_pet(pet):
        print(f'ID: {pet.id} - Nome: {pet.nome}')

