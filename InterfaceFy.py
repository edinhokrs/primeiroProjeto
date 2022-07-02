import PySimpleGUI as sg
import webbrowser

play1 = 'https://www.youtube.com/watch?v=mDp5zbQP_qI&t=521s'
play2 = 'https://www.youtube.com/watch?v=zVj0p-DT6RM&list=PLvW7twb4hHB4xBHwHhtn3kViyhEFbw4k2'
play3 = 'https://www.youtube.com/watch?v=eXp86zDQKjY'
sg.theme('Black')


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text(size=(42, 30)), sg.Button('Froid', size=(15, 5), key='playlist1'), sg.Button(
                'BK', size=(15, 5), key='playlist2'), sg.Button('Oasis', size=(15, 5), key='playlist3'), sg.Text(size=(50, 30))]
        ]
        self.janela = sg.Window("Playlist Spotify",).layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            if self.values == sg.WIN_CLOSED:
                break
            if self.button == 'playlist1':
                print("Toca Froid!")
                webbrowser.get(
                    'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(play1)
            if self.button == 'playlist2':
                print('Toca BK!')
                webbrowser.get(
                    'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(play2)

            if self.button == 'playlist3':
                print('Toca Oasis!')
                webbrowser.get(
                    'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(play3)


tela = TelaPython()
tela.iniciar()
