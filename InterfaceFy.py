import PySimpleGUI as sg


sg.theme('Black')


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text(size=(15, 1)), sg.Button('Playlist 1', size=(15, 5), key='playlist1'), sg.Button(
                'Playlist 2', size=(15, 5), key='playlist2'), sg.Button('Playlist 3', size=(15, 5), key='playlist3'), sg.Text(size=(15, 1))]
        ]
        self.janela = sg.Window("Playlist Spotify",).layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            if self.values == sg.WIN_CLOSED:
                break


tela = TelaPython()
tela.iniciar()
