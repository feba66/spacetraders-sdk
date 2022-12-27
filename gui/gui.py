import PySimpleGUI as sg
from main import Main


class SpaceTradersGUI:
    THEME = "darkteal10"
    RECENT_ACC_PATH = "recent_accs.csv"
    main: Main
    window:sg.Window
    def __init__(self) -> None:
        sg.theme(SpaceTradersGUI.THEME)
        self.main = Main()
        self.main.load_recent(SpaceTradersGUI.RECENT_ACC_PATH)

    @property
    def register_layout(self):
        return [[sg.Text("Name"), sg.InputText(key="-name-", size=(30, 10))],
                [sg.Text("Faction"), sg.DropDown(
                    values=["a", "b", "c"], key="-faction-", size=(27, 10))],
                [sg.Button("Register",k="-register-"), sg.Button("To Login", k="-toLogin-")]]

    @property
    def login_layout(self):
        return [[sg.Text("Token"), sg.InputText(size=(30, 10),k="-token-")],
                [sg.Button("Login",k="-login-"), sg.Button("To Register", k="-toRegister-")]]

    @property
    def game_layout(self):
        return [[]]
    @property
    def get_pins(self):
        return [sg.pin(sg.Column(self.register_layout, key="-l1-", visible=True)),
                sg.pin(sg.Column(self.login_layout, key="-l2-", visible=False))]

    def run(self):
        self.window = sg.Window("Space Traders GUI",layout=[[self.get_pins]],margins=(10,10))
        while True:
            event, values = self.window.read()
            print(event)
            if event == "-login-":
                print(values["-token-"])
                self.main.login(values["-token-"])
            elif event == "-register-":
                print(values["-name-"])
                print(values["-faction-"])
            elif event == "-toLogin-":
                self.window["-l1-"].update(visible=False)
                self.window["-l2-"].update(visible=True)
                self.window.refresh()
            elif event == "-toRegister-":
                self.window["-l2-"].update(visible=False)
                self.window["-l1-"].update(visible=True)
                self.window.refresh()
            elif event == sg.WIN_CLOSED:
                break

        self.window.close()
        


if __name__ == "__main__":

    gui = SpaceTradersGUI()
    gui.run()

    exit()
    sg.theme("darkteal10")
    register_layout = [[sg.Text("Name"), sg.InputText(key="-name-", size=(30, 10))],
                       [sg.Text("Faction"), sg.DropDown(
                           values=["a", "b", "c"], key="-faction-", size=(27, 10))],
                       [sg.Button("Register"), sg.Button("To Login", k="-toLogin-")]]
    login_layout = [[sg.Text("Token"), sg.InputText(size=(30, 10))],
                    [sg.Button("Login"), sg.Button("To Register", k="-toRegister-")]]
    # first_layout = [[sg.Frame("Register", register_layout)],
    #           [sg.Frame("Login", login_layout)]]
    # window = sg.Window(title="Space Traders Client", layout=[[sg.Column(register_layout,key="-l1-",visible=True)],[sg.Column(login_layout,key="-l2-",visible=False)]], margins=(10, 10))
    window = sg.Window(title="Space Traders Client", layout=[[sg.pin(sg.Column(
        register_layout, key="-l1-", visible=True)), sg.pin(sg.Column(login_layout, key="-l2-", visible=False))]], margins=(10, 10))

    while True:
        event, values = window.read()
        print(event)
        if event == "Register":
            print(values["-name-"])
            print(values["-faction-"])
        elif event == "-toLogin-":
            window["-l1-"].update(visible=False)
            window["-l2-"].update(visible=True)
        elif event == "-toRegister-":
            window["-l2-"].update(visible=False)
            window["-l1-"].update(visible=True)
        elif event == sg.WIN_CLOSED:
            break

    window.close()
