messages = 0
import PySimpleGUI as sg
window = sg.Window(title="Message Maker", layout=[[sg.InputText('Insert some Input Text!')], [sg.Button('Done'), sg.Button('Exit')], margins=(350, 150)).read()
messages += 1
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Done':
        sg.Popup(title="Message" + str(messages), layout=[[sg.InputText(values[0])], [sg.Button('Close')]], margins=(100, 50)).read()
        messages += 1
