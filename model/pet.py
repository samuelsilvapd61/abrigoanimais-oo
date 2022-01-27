class Animal:
    def __init__(self):
        self.id = 0
        self.nome = ''

    def brincar(self):
        pass


class Cachorro(Animal):
    def brincar(self):
        print(f'{self.nome} está latindo !')


class Gato(Animal):
    def brincar(self):
        print(f'{self.nome} está miando !')


class Passaro(Animal):
    def brincar(self):
        print(f'{self.nome} está cantando !')


class Peixe(Animal):
    def brincar(self):
        print(f'{self.nome} está pulando o anel !')
