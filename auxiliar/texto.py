class Texto:

    @staticmethod
    def linha():
        print('-' * 100)

    @staticmethod
    def titulo(mensagem='Mensagem inexistente'):
        Texto.linha()
        print(f'{mensagem:^100}')
        Texto.linha()

    @staticmethod
    def menu_opcoes(*opcoes):
        mensagem = ''
        for opcao in opcoes:
            mensagem += f'{opcao} | '

        print(mensagem[0:len(mensagem) - 3])

        return int(input('Digite a opção desejada: '))

