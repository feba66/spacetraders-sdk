from pprint import pprint
import PySimpleGUI as sg
from main import Main, Account
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PySimpleGUI.PySimpleGUI import Canvas


class SpaceTradersGUI:
    THEME = "darkteal10"
    main: Main
    window: sg.Window
    treedata:sg.TreeData
    canvases:dict[Canvas.TKCanvas,FigureCanvasTkAgg]
    
    def __init__(self) -> None:
        sg.theme(SpaceTradersGUI.THEME)
        self.main = Main()
        self.main.load_recent()
        self.treedata=sg.TreeData()
        self.canvases = {}

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
                # ,
                [sg.TabGroup([[sg.Tab("Agent", self.get_agent_layout(), k="-agenttab-"),
                               sg.Tab("Ships", self.get_ship_layout(), k="-shiptab-"),
                               sg.Tab("System", [[sg.Canvas(expand_x=True,expand_y=True,k="-systemcanvas-")]], k="-systemtab-"),
                               sg.Tab("Systems", [[sg.Canvas(expand_x=True,expand_y=True,k="-systemscanvas-")]], k="-systemstab-"),
                               ]],
                             enable_events=True,
                             k="-gametabgroup-",
                             size=(600,500)),
                ]]

    def get_agent_layout(self):
        return [[sg.Text("symbol", k="-agentsymbol-")]]

    def update_agent(self):
        agent = self.main.get_agent()
        string = f"Name: {agent.symbol}\nAccount ID: {agent.accountId}\nHeadquarter: {agent.headquarters}\nCredits: {agent.credits}"
        self.window["-agentsymbol-"].update(value=string)

    def get_ship_layout(self):
        return [[sg.Tree(data=self.treedata, headings=['Current', 'Maximum', '3'], change_submits=True, auto_size_columns=True, header_border_width=4,
             # header_relief=RELIEF_GROOVE,
             key='-tree-', show_expanded=True,expand_x=True,expand_y=True )]]

    def update_ships(self):
        ships = self.main.get_ships()
        self.treedata =sg.TreeData()
        for sname in ships:
            ship = ships[sname]
            k = f"-{ship.symbol}-"

            status = ship.nav.status != ship.nav.status.DOCKED
            self.treedata.insert("",k,ship.symbol,[ship.nav.status.name,ship.nav.waypointSymbol,ship.nav.route.arrival if status else ""])
            self.treedata.insert(k,k+"stats-","Stats",[])
            self.treedata.insert(k+"stats-",k+"stats-cons-","Consumables",[])

            self.treedata.insert(k+"stats-cons-",k+"stats-cons-fuel","Fuel",[ship.fuel.current,ship.fuel.capacity])
            self.treedata.insert(k+"stats-cons-",k+"stats-cons-crew","Crew",[ship.crew.current,ship.crew.capacity])
            cur_power = ship.engine.requirements.power + ship.frame.requirements.power \
                + sum([x.requirements.power for x in ship.modules]) + sum([x.requirements.power for x in ship.mounts]) 
            self.treedata.insert(k+"stats-cons-",k+"stats-cons-powr","Power",[cur_power,ship.reactor.powerOutput])
            self.treedata.insert(k+"stats-",k+"stats-frame","Frame",[ship.frame.name])
            self.treedata.insert(k+"stats-",k+"stats-engine","Engine",[ship.engine.name,ship.engine.speed])
            self.treedata.insert(k+"stats-",k+"stats-reactor","Reactor",[ship.reactor.name,ship.reactor.powerOutput])
            self.treedata.insert(k+"stats-",k+"stats-role","Role",[ship.registration.role])

            self.treedata.insert(k,k+"cargo-","Cargo",[ship.cargo.units,ship.cargo.capacity])
            for c in ship.cargo.inventory:
                self.treedata.insert(k+"cargo-",k+f"cargo-{c.symbol}-",c.name,[c.units])

            self.treedata.insert(k,k+"mounts-","Mounts",[len(ship.mounts),ship.frame.mountingPoints])
            for m in ship.mounts:
                self.treedata.insert(k+"mounts-",k+f"mounts-{m.symbol}-",m.name,[m.strength if m.strength else None])

            self.treedata.insert(k,k+"modules-","Modules",[len(ship.modules),ship.frame.moduleSlots])
            for m in ship.modules:
                self.treedata.insert(k+"modules-",k+f"modules-{m.symbol}-",m.name,[m.capacity if m.capacity else m.range if m.range else None])
            
        pprint(ships)
        self.window["-tree-"].update(values=self.treedata)
    
    def draw_fig(self, canvas, fig):
        if canvas not in self.canvases:
            self.canvases[canvas]=FigureCanvasTkAgg(fig, canvas)
        figure_canvas_agg =self.canvases[canvas]
        
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    @property
    def get_pins(self):
        return [sg.pin(sg.Column(self.register_layout, key="-l1-", visible=True)),
                sg.pin(sg.Column(self.login_layout, key="-l2-", visible=False)),
                sg.pin(sg.Column(self.game_layout, key="-l3-", visible=False))]

    def run(self):
        self.window = sg.Window("Space Traders GUI", layout=[[self.get_pins]], margins=(10, 10), finalize=True,resizable=False)
        self.window.bind('<Configure>', "Resize_Event")
        while True:
            event, values = self.window.read()
            print(event)
            if event == "Resize_Event":
                # new_size = (int(self.window.size[0] * 0.9), int(self.window.size[1] * 0.9))
                # old_size = self.window["-gametabgroup-"].get_size()
                # self.window["-gametabgroup-"].set_size(old_size)
                # old_size = self.window["-gametabgroup-"].get_size()
                # self.window["-gametabgroup-"].set_size(old_size)
                self.window.Refresh()
                pass
            elif event == "-login-":
                # print(values["-token-"])
                if self.main.login(values["-token-"].replace("\n","")):
                    self.window["-l2-"].update(visible=False)
                    self.window["-l3-"].update(visible=True)
                    self.window["-logintext-"].update(
                        value=f"Youre logged in as {self.main.get_recent().name}")
                    self.update_agent()
            elif event == "-gametabgroup-":
                e = self.window["-gametabgroup-"].get()
                if e == "-shiptab-":
                    self.update_ships()
                elif e == "-agenttab-":
                    self.update_agent()
                elif e == "-systemtab-":
                    self.draw_fig(self.window["-systemcanvas-"].TKCanvas,self.main.get_system_plot("X1-UV97"))
                elif e == "-systemstab-":
                    self.draw_fig(self.window["-systemscanvas-"].TKCanvas,self.main.get_systems_plot())
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
