from datetime import datetime
from pprint import pprint
import PySimpleGUI as sg
from main import Main
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PySimpleGUI.PySimpleGUI import Canvas


class SpaceTradersGUI:
    THEME = "darkteal10"
    main: Main
    window: sg.Window
    treedata: sg.TreeData
    system_treedata: sg.TreeData
    canvases: dict[Canvas.TKCanvas, FigureCanvasTkAgg]

    last_shipyards = []
    last_shipyardships = []
    last_table_cargo = []

    # region bools
    _shipdrop_populated = False
    _shipnavdrop_populated = False
    _shipyarddrop_populated = False
    # endregion
    # region times
    _shipdrop_populated_time = None
    # endregion

    def __init__(self) -> None:
        sg.theme(SpaceTradersGUI.THEME)
        self.main = Main()
        self.main.load_recent()
        self.treedata = sg.TreeData()
        self.canvases = {}
        self.last_surveydata = []

    @property
    def register_layout(self):
        return [[sg.Text("Name"), sg.InputText(key="-name-", size=(30, 10))],
                [sg.Text("Faction"), sg.DropDown(
                    values=["COSMIC", "VOID", "GALACTIC", "QUANTUM", "DOMINION"], key="-faction-", size=(27, 10))],
                [sg.Button("Register", k="-register-"), sg.Button("To Login", k="-toLogin-")]]

    @property
    def login_layout(self):
        recent = self.main.get_recent()
        default = recent.token if recent else ""
        return [[sg.Text("Token"), sg.InputText(size=(30, 10), k="-token-", default_text=default)],
                [sg.Button("Login", k="-login-"), sg.Button("To Register", k="-toRegister-")]]

    @property
    def game_layout(self):
        return [[sg.Text("Youre logged in now", k="-logintext-"), sg.Push(), sg.Text("Credits: ", k="-creditstext-", size=(16, 1))],
                # ,
                [sg.TabGroup([[sg.Tab("Agent", self.get_agent_layout(), k="-agenttab-"),
                               sg.Tab("Ships", self.get_ships_layout(), k="-shipstab-"),
                               sg.Tab("Ship", self.get_ship_layout(), k="-shiptab-"),
                               sg.Tab("Shipyards", self.get_shipyards_layout(), k="-shipyardtab-"),
                               sg.Tab("System", self.get_system_layout(), k="-systemtab-"),
                               sg.Tab("Systems", [
                                      [sg.Canvas(expand_x=True, expand_y=True, k="-systemscanvas-")]], k="-systemstab-"),
                               ]],
                             enable_events=True,
                             k="-gametabgroup-",
                             size=(1000, 600)),
                 ]]

    def get_agent_layout(self):
        return [[sg.Column(
            [[sg.Frame("Agent", [[sg.Text("symbol", k="-agentsymbol-")]])],
                [sg.Frame("Contracts", [[sg.Text("contract", k="-contractsymbol-")]])]
             ], scrollable=True, vertical_scroll_only=True, expand_x=True, expand_y=True)

        ]]

    def update_agent(self):
        agent = self.main.get_agent()
        string = f"Name: {agent.symbol}\nAccount ID: {agent.accountId}\nHeadquarter: {agent.headquarters}\nCredits: {agent.credits}"
        self.window["-agentsymbol-"].update(value=string)

    def update_contract(self):
        contracts = self.main.get_contracts()
        string = ""
        first = True
        for co in contracts:
            c = contracts[co]
            if not first:
                string += "\n\n"
            else:
                first = False
            string += f"Id: {c.id}\n  Accepted: {c.accepted}\n  Fulfilled: {c.fulfilled}\n  Faction: {c.factionSymbol}\n  Expiration: {c.expiration}\n  Type: {c.type}\n  Terms:\n    Deadline: {c.terms.deadline}\n    onAccepted: {c.terms.payment.onAccepted}\n    onFulfilled: {c.terms.payment.onFulfilled}\n    Deliver:"

            firstd = True
            if not firstd:
                string += "\n"
            else:
                firstd = False
            for d in c.terms.deliver:
                string += f"\n      {d.tradeSymbol}:\n        Units: {d.unitsFulfilled}/{d.unitsRequired}\n        To: {d.destinationSymbol}"
        self.window["-contractsymbol-"].update(value=string)

    def get_ships_layout(self):
        return [[sg.Tree(data=self.treedata, headings=['Current', 'Maximum', '3'], change_submits=True, auto_size_columns=True, header_border_width=4,
                         # header_relief=RELIEF_GROOVE,
                         key='-tree-', show_expanded=True, expand_x=True, expand_y=True)]]

    def update_ships_tree(self):
        ships = self.main.get_ships()
        self.treedata = sg.TreeData()
        for ship in ships.values():
            k = f"-{ship.symbol}-"

            status = ship.nav.status != ship.nav.status.DOCKED
            self.treedata.insert("", k, ship.symbol, [
                                 ship.nav.status.name, ship.nav.waypointSymbol, ship.nav.route.arrival if status else ""])
            self.treedata.insert(k, k+"stats-", "Stats", [])
            self.treedata.insert(k+"stats-", k+"stats-cons-", "Consumables", [])

            self.treedata.insert(k+"stats-cons-", k+"stats-cons-fuel", "Fuel",
                                 [ship.fuel.current, ship.fuel.capacity])
            self.treedata.insert(k+"stats-cons-", k+"stats-cons-crew", "Crew",
                                 [ship.crew.current, ship.crew.capacity])
            cur_power = ship.engine.requirements.power + ship.frame.requirements.power \
                + sum([x.requirements.power for x in ship.modules]) + \
                sum([x.requirements.power for x in ship.mounts])
            self.treedata.insert(k+"stats-cons-", k+"stats-cons-powr",
                                 "Power", [cur_power, ship.reactor.powerOutput])
            self.treedata.insert(k+"stats-", k+"stats-frame", "Frame", [ship.frame.name])
            self.treedata.insert(k+"stats-", k+"stats-engine", "Engine",
                                 [ship.engine.name, ship.engine.speed])
            self.treedata.insert(k+"stats-", k+"stats-reactor", "Reactor",
                                 [ship.reactor.name, ship.reactor.powerOutput])
            self.treedata.insert(k+"stats-", k+"stats-role", "Role", [ship.registration.role])

            self.treedata.insert(k, k+"cargo-", "Cargo", [ship.cargo.units, ship.cargo.capacity])
            for c in ship.cargo.inventory:
                self.treedata.insert(k+"cargo-", k+f"cargo-{c.symbol}-", c.name, [c.units])

            self.treedata.insert(k, k+"mounts-", "Mounts",
                                 [len(ship.mounts), ship.frame.mountingPoints])
            for m in ship.mounts:
                self.treedata.insert(
                    k+"mounts-", k+f"mounts-{m.symbol}-", m.name, [m.strength if m.strength else None])

            self.treedata.insert(k, k+"modules-", "Modules",
                                 [len(ship.modules), ship.frame.moduleSlots])
            for m in ship.modules:
                self.treedata.insert(k+"modules-", k+f"modules-{m.symbol}-", m.name, [
                                     m.capacity if m.capacity else m.range if m.range else None])
        self.window["-tree-"].update(values=self.treedata)

    def get_ship_layout(self):
        return [[sg.Drop([], k="-shipdrop-", s=(20, 10), enable_events=True)],
                [sg.Text("ship", k="-shiptxt-")],
                [sg.Text("fuel", k="-shipfueltxt-")],
                [sg.Text("shipstatus", k="-shipstatustxt-"), sg.ProgressBar(10000,
                                                                            k="-shipstatusbar-", size=(100, 10), visible=False)],
                [sg.Text("Cooldown: "), sg.ProgressBar(
                    10000, k="-shipcooldownbar-", size=(100, 10), visible=False)],
                [sg.Button("Dock", k="-btndock-"), sg.Button("Orbit", k="-btnorbit-"), sg.Button("Navigate to:", k="-btnnavigate-"), sg.Drop([], k="-shipnavdrop-", s=(20, 10)),
                 sg.Button("Excavate", k="-btnexcavate-"), sg.Button("Survey",
                                                                     k="-btnsurvey-"), sg.Button("Refuel", k="-btnrefuel-"),
                 sg.Button("Sell", k="-btnsell-"), sg.Button("Jettison", k="-btnjettison-"), sg.Button("Deliver", k="-btndeliver-")],
                [sg.Table([], ["Symbol", "Units"], k="-shipcargotable-", expand_x=True)],
                [sg.Table([], ["Symbol", "Size", "Deposits", "sig"], k="-shipsurveytable-",
                          expand_x=True, col_widths=[120, 100, 570, 170])],
                [sg.Button("Delete survey", k="-btndelsurvey-")]
                ]

    def get_system_layout(self):
        return [[sg.Tree(data=self.treedata, headings=['st', 'nd', 'th'], change_submits=True, auto_size_columns=False, header_border_width=4,
                    # header_relief=RELIEF_GROOVE,
                    key='-systemtree-', show_expanded=True, expand_x=True, expand_y=True)]]

    def update_system_tree(self):
        self.system_treedata = sg.TreeData()
        system = self.main.get_waypoints("X1-DF55")
        for w in system:
            print(w)
            k = f"-{w.symbol}-"
            self.system_treedata.insert("",k,w.symbol,[str(w.type)])

            if len(w.traits)>0:
                self.system_treedata.insert(k, k+"traits-", "Traits", [])
                for t in w.traits:
                    self.system_treedata.insert(k+"traits-", k+"traits-"+str(t.symbol), str(t.symbol), [t.description])

            if len(w.orbitals)>0:
                self.system_treedata.insert(k, k+"orbitals-", "Orbitals", [])
                for o in w.orbitals:
                    self.system_treedata.insert(k+"orbitals-", k+"orbitals-"+str(o.symbol), str(o.symbol), [])
                    
        # ships = self.main.get_ships()
        # for ship in ships.values():
        #     k = f"-{ship.symbol}-"

        #     status = ship.nav.status != ship.nav.status.DOCKED
        #     self.treedata.insert("", k, ship.symbol, [
        #                          ship.nav.status.name, ship.nav.waypointSymbol, ship.nav.route.arrival if status else ""])
        #     self.treedata.insert(k, k+"stats-", "Stats", [])
        #     self.treedata.insert(k+"stats-", k+"stats-cons-", "Consumables", [])

        #     self.treedata.insert(k+"stats-cons-", k+"stats-cons-fuel", "Fuel",
        #                          [ship.fuel.current, ship.fuel.capacity])
        #     self.treedata.insert(k+"stats-cons-", k+"stats-cons-crew", "Crew",
        #                          [ship.crew.current, ship.crew.capacity])
        #     cur_power = ship.engine.requirements.power + ship.frame.requirements.power \
        #         + sum([x.requirements.power for x in ship.modules]) + \
        #         sum([x.requirements.power for x in ship.mounts])
        #     self.treedata.insert(k+"stats-cons-", k+"stats-cons-powr",
        #                          "Power", [cur_power, ship.reactor.powerOutput])
        #     self.treedata.insert(k+"stats-", k+"stats-frame", "Frame", [ship.frame.name])
        #     self.treedata.insert(k+"stats-", k+"stats-engine", "Engine",
        #                          [ship.engine.name, ship.engine.speed])
        #     self.treedata.insert(k+"stats-", k+"stats-reactor", "Reactor",
        #                          [ship.reactor.name, ship.reactor.powerOutput])
        #     self.treedata.insert(k+"stats-", k+"stats-role", "Role", [ship.registration.role])

        #     self.treedata.insert(k, k+"cargo-", "Cargo", [ship.cargo.units, ship.cargo.capacity])
        #     for c in ship.cargo.inventory:
        #         self.treedata.insert(k+"cargo-", k+f"cargo-{c.symbol}-", c.name, [c.units])

        #     self.treedata.insert(k, k+"mounts-", "Mounts",
        #                          [len(ship.mounts), ship.frame.mountingPoints])
        #     for m in ship.mounts:
        #         self.treedata.insert(
        #             k+"mounts-", k+f"mounts-{m.symbol}-", m.name, [m.strength if m.strength else None])

        #     self.treedata.insert(k, k+"modules-", "Modules",
        #                          [len(ship.modules), ship.frame.moduleSlots])
        #     for m in ship.modules:
        #         self.treedata.insert(k+"modules-", k+f"modules-{m.symbol}-", m.name, [
        #                              m.capacity if m.capacity else m.range if m.range else None])
        self.window["-systemtree-"].update(values=self.system_treedata)

    def update_ship(self):
        if not self._shipdrop_populated or self._shipdrop_populated_time and (datetime.utcnow()-self._shipdrop_populated_time) > 300:
            ships = self.main.get_ships()
            self.window["-shipdrop-"].update(values=list(ships.keys()))
            self._shipdrop_populated = True

        if not self._shipnavdrop_populated and self.main.selected_ship != "":
            s = self.main.get_ships()[self.main.selected_ship]
            waypoints = self.main.get_waypoints(s.nav.systemSymbol)
            self.window["-shipnavdrop-"].update(values=[w.symbol for w in waypoints])
            self._shipnavdrop_populated = True

        if self.main.selected_ship != "":
            s = self.main.get_ships()[self.main.selected_ship]
            self.window["-shiptxt-"].update(value=f"Name: {s.symbol}")
            self.window["-shipfueltxt-"].update(
                value=f"Fuel: {s.fuel.current}/{s.fuel.capacity}\nCargo: {s.cargo.units}/{s.cargo.capacity}")
            remaining = ""
            if s.nav.status == s.nav.status.IN_TRANSIT:
                arrive = self.main.parse_time(s.nav.route.arrival)
                start = self.main.parse_time(s.fuel.consumed.timestamp)
                diff = self.main.get_time_diff(arrive, datetime.utcnow())
                if diff < 0:
                    percentLeft = 0
                total = self.main.get_time_diff(arrive, start)
                remaining = f" Remaining: {max(round(diff,5),0)}"
                percentLeft = diff/total
                self.window["-shipstatusbar-"].update(
                    current_count=int((1-percentLeft)*10000), visible=True)
            else:
                self.window["-shipstatusbar-"].update(visible=False)
            self.window["-shipstatustxt-"].update(
                value=f"Status: {s.nav.status.name} At/To: {s.nav.waypointSymbol}{remaining}")
            cargo = [(c.symbol, c.units) for c in s.cargo.inventory]
            if cargo != self.last_table_cargo:
                self.window["-shipcargotable-"].update(values=cargo)
                self.last_table_cargo = cargo
            cooldown = self.main.get_cooldown(self.main.selected_ship)
            if cooldown:
                end = self.main.parse_time(cooldown.expiration)
                diff = self.main.get_time_diff(end, datetime.utcnow())
                if diff <= 0:
                    percentLeft = 0
                else:
                    percentLeft = diff/cooldown.totalSeconds
                self.window["-shipcooldownbar-"].update(
                    current_count=int((1-percentLeft)*10000), visible=True)
            else:
                self.window["-shipcooldownbar-"].update(visible=False)
            surveys = self.main.get_surveys()
            surveydata = []
            for s in surveys:
                if self.main.parse_time(s.expiration) < datetime.utcnow():
                    self.main.remove_survey(s.signature)
                    continue
                deposits = list(x.symbol for x in s.deposits)
                surveydata.append((s.symbol, s.size, deposits, s.signature))
            if self.last_surveydata != surveydata:
                self.window["-shipsurveytable-"].update(values=surveydata)
                self.last_surveydata = surveydata

    def get_shipyards_layout(self):
        return [[sg.Column([
            [sg.Drop([], k="-shipyarddrop-", size=(20, 1))],
            [sg.Text("", k="-shipyardtext-")],
            [sg.Drop([], "Select Shipyard first", k="-shipyardship-", size=(20, 1))],
            [sg.Button("Buy", k="-buyship-")]
        ],
            scrollable=True, vertical_scroll_only=True,
            expand_x=True, expand_y=True)]]

    def update_shipyards(self):
        if not self._shipyarddrop_populated:
            locs = {}
            for x in self.main.get_ships().values():
                locs[self.main.st.system_sym_f_wayp(x.nav.waypointSymbol)] = 1
            shipyards = []
            for l in locs:
                wp = self.main.get_waypoints(l)
                for w in wp:
                    if "SHIPYARD" in [x.symbol.name for x in w.traits]:
                        shipyards.append(w.symbol)
            if shipyards != self.last_shipyards:
                self.window["-shipyarddrop-"].update(values=shipyards)
                self.last_shipyards = shipyards
            self._shipyarddrop_populated = True
        g = self.window["-shipyarddrop-"].get()
        if g in self.last_shipyards:
            sy = self.main.get_shipyard(g)
            if [x.name for x in sy.shipTypes] != self.last_shipyardships:
                self.window["-shipyardship-"].update(values=[x.name for x in sy.shipTypes])
                self.last_shipyardships = [x.name for x in sy.shipTypes]
            s = self.window["-shipyardship-"].get()
            if s in self.last_shipyardships:
                self.window["-shipyardtext-"].update(value=s)

    def draw_fig(self, canvas, fig):
        if canvas not in self.canvases:
            self.canvases[canvas] = FigureCanvasTkAgg(fig, canvas)
        figure_canvas_agg = self.canvases[canvas]

        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    @property
    def get_pins(self):
        return [sg.pin(sg.Column(self.register_layout, key="-l1-", visible=False)),
                sg.pin(sg.Column(self.login_layout, key="-l2-", visible=True)),
                sg.pin(sg.Column(self.game_layout, key="-l3-", visible=False))]

    def update(self, manual=False):
        if self.main._is_logged_in:
            self.window["-logintext-"].update(
                value=f"Youre logged in as {self.main.get_recent().name}")
            self.window["-creditstext-"].update(value=f"Credits: {self.main.get_agent().credits}")
            e = self.window["-gametabgroup-"].get()
            if e == "-shipstab-":
                self.update_ships_tree()
            elif e == "-shiptab-":
                self.update_ship()
            elif e == "-shipyardtab-":
                self.update_shipyards()
            elif e == "-agenttab-":
                self.update_agent()
                self.update_contract()
            elif e == "-systemtab-" and manual:
                self.update_system_tree()
                # self.draw_fig(self.window["-systemcanvas-"].TKCanvas,
                #               self.main.get_system_plot("X1-DF55"))
            elif e == "-systemstab-" and manual:
                self.draw_fig(self.window["-systemscanvas-"].TKCanvas,
                              self.main.get_systems_plot())

    def run(self):
        self.window = sg.Window("Space Traders GUI", layout=[[self.get_pins]], margins=(
            10, 10), finalize=True, resizable=False)
        while True:
            event, values = self.window.read(timeout=50, timeout_key="-update-")

            if event == "-update-":
                self.update()

            elif event == "-gametabgroup-":
                self.update(True)

            elif event == "-shipdrop-":
                self.main.select_ship(values["-shipdrop-"])
                self.update(True)

            elif event == "-btndock-":
                self.main.dock_ship(self.main.selected_ship)
                self.update(True)

            elif event == "-btnorbit-":
                self.main.orbit_ship(self.main.selected_ship)
                self.update(True)

            elif event == "-btnnavigate-":
                self.main.navigate_ship(self.main.selected_ship, values["-shipnavdrop-"])
                self.update(True)

            elif event == "-btnsurvey-":
                self.main.survey(self.main.selected_ship)
                self.update(True)

            elif event == "-btnexcavate-":
                if len(values["-shipsurveytable-"]) == 1:
                    for s in self.main.get_surveys():
                        if s.signature == self.last_surveydata[values["-shipsurveytable-"][0]][3]:
                            survey = s
                            break
                    self.main.excavate(self.main.selected_ship, survey)
                else:
                    self.main.excavate(self.main.selected_ship)
                self.update(True)

            elif event == "-btnrefuel-":
                self.main.refuel(self.main.selected_ship)
                self.update(True)

            elif event == "-btnsell-" or event == "-btnjettison-":
                for i in values["-shipcargotable-"]:
                    c = self.last_table_cargo[i]
                    if event == "-btnsell-":
                        self.main.sell_good(self.main.selected_ship, c[0], c[1])
                    elif event == "-btnjettison-":
                        self.main.jettison_good(self.main.selected_ship, c[0], c[1])
                self.update(True)

            elif event == "-btndeliver-" and len(values["-shipcargotable-"]) == 1:
                co = self.main.get_contracts()
                if len(co.keys()) == 1:
                    k = list(co.keys())[0]
                    c = self.last_table_cargo[values["-shipcargotable-"][0]]
                    for d in co[k].terms.deliver:
                        if c[0] == d.tradeSymbol:
                            self.main.deliver(co[k].id, self.main.selected_ship, c[0], c[1])
                else:
                    raise NotImplementedError()

            elif event == "-btndelsurvey-":
                for s in [self.last_surveydata[x][3] for x in values["-shipsurveytable-"]]:
                    if s in [x.signature for x in self.main.get_surveys()]:
                        self.main.remove_survey(s)
                        break

            elif event == "-buyship-" and self.window["-shipyardship-"].get() in self.last_shipyardships:
                self.main.buy_ship(self.window["-shipyarddrop-"].get(),
                                   self.window["-shipyardship-"].get())

            elif event == "-login-":
                if self.main.login(values["-token-"].replace("\n", "")):
                    self.window["-l2-"].update(visible=False)
                    self.window["-l3-"].update(visible=True)
                    self.update(True)

            elif event == "-register-":
                print(values["-name-"])
                print(values["-faction-"])
                self.main.register(values["-name-"], values["-faction-"])

            elif event == "-toLogin-":
                self.window["-l1-"].update(visible=False)
                self.window["-l2-"].update(visible=True)

            elif event == "-toRegister-":
                self.window["-l2-"].update(visible=False)
                self.window["-l1-"].update(visible=True)

            elif event == sg.WIN_CLOSED:
                break

            else:
                print(event)

        self.window.close()


if __name__ == "__main__":

    gui = SpaceTradersGUI()
    gui.run()
