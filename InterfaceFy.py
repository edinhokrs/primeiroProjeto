import PySimpleGUI as sg


sg.theme('Black')


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Button('Playlist 1', size=(15, 5), key='playlist1'), sg.Button(
                'Playlist 2', size=(15, 5), key='playlist2'), sg.Button('Playlist 3', size=(15, 5), key='playlist3')]
        ]
        janela = sg.Window("Playlist Spotify",).layout(layout)
        self.button, self.values = janela.read()


tela = TelaPython()
