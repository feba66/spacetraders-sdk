import PySimpleGUI as sg
from main import Main, Account
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SpaceTradersGUI:
    THEME = "darkteal10"
    main: Main
    window: sg.Window

    def __init__(self) -> None:
        sg.theme(SpaceTradersGUI.THEME)
        self.main = Main()
        self.main.load_recent()

    @property
    def register_layout(self):
        return [[sg.Text("Name"), sg.InputText(key="-name-", size=(30, 10))],
                [sg.Text("Faction"), sg.DropDown(
                    values=["a", "b", "c"], key="-faction-", size=(27, 10))],
                [sg.Button("Register", k="-register-"), sg.Button("To Login", k="-toLogin-")]]

    @property
    def login_layout(self):
        recent = self.main.get_recent()
        default = recent.token if recent else ""
        return [[sg.Text("Token"), sg.InputText(size=(30, 10), k="-token-", default_text=default)],
                [sg.Button("Login", k="-login-"), sg.Button("To Register", k="-toRegister-")]]

    @property
    def game_layout(self):
        return [[sg.Text("Youre logged in now", k="-logintext-")],
                [sg.Canvas(size=(300, 300),k="-canvas-")]]


    

    def draw_fig(self,canvas,fig):
        figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    @property
    def get_pins(self):
        return [sg.pin(sg.Column(self.register_layout, key="-l1-", visible=True)),
                sg.pin(sg.Column(self.login_layout, key="-l2-", visible=False)),
                sg.pin(sg.Column(self.game_layout, key="-l3-", visible=False))]

    def run(self):
        self.window = sg.Window("Space Traders GUI", layout=[[self.get_pins]], margins=(10, 10),finalize=True)
        
        
        while True:
            event, values = self.window.read()
            print(event)
            if event == "-login-":
                # print(values["-token-"])
                if self.main.login(values["-token-"]):
                    self.window["-l2-"].update(visible=False)
                    self.window["-l3-"].update(visible=True)
                    self.window["-logintext-"].update(value=f"Youre logged in as {self.main.get_recent().name}")
                    self.draw_fig(self.window["-canvas-"].TKCanvas,self.main.get_system_plot("X1-UV97"))
            elif event == "-register-":
                print(values["-name-"])
                print(values["-faction-"])
            elif event == "-toLogin-":
                self.window["-l1-"].update(visible=False)
                self.window["-l2-"].update(visible=True)
            elif event == "-toRegister-":
                self.window["-l2-"].update(visible=False)
                self.window["-l1-"].update(visible=True)
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
