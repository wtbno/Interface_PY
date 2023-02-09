import PySimpleGUI as sg


class InterfacePy:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(6, 0)), sg.Input(
                size=(30, 0), key='nome')],
            # Key funciona como um identificador do elemento
            # Estilização do elemento é realizada dentro dos ()
            [sg.Text('Idade', size=(6, 0)), sg.Input(
                size=(30, 0), key='idade')],
            [sg.Text('Gênero', size=(6, 0)), sg.Input(
                size=(30, 0), key='genero')],
            [sg.Text('Cidade', size=(6, 0)), sg.Input(
                size=(30, 0), key='cidade')],
            [sg.Text('Selecione seu e-mail')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox(
                'Hotmail', key='hotmail'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('Enviar dados')],
        ]
        # Janela
        janela = sg.Window("Dados").layout(layout)
        # Atributo recebe o layout criado acima

        self.button, self.values = janela.Read()
        # Run packing = transfere informações de um local para mais de uma var.

    # Criação do método iniciar
    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        genero = self.values['genero']
        cidade = self.values['cidade']
        aceita_gmail = self.values['gmail']
        aceita_hotmail = self.values['hotmail']
        aceita_yahoo = self.values['yahoo']
        # sempre passando o valor que foi informado dentro do key
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'genero: {genero}')
        print(f'cidade: {cidade}')
        print(f'aceita_gmail: {aceita_gmail}')
        print(f'aceita_hotmail: {aceita_hotmail}')
        print(f'aceita_yahoo: {aceita_yahoo}')


tela = InterfacePy()
tela.Iniciar()
