from dataclasses import dataclass
from datetime import datetime
from pprint import pprint
import time
import PySimpleGUI as sg
import os
import sys
import matplotlib.pyplot as plt

# sorry
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from api import SpaceTraders

@dataclass
class Account:
    name: str
    token: str
    lastLogin: datetime

    def toCSV(self):
        return f"{self.name};{self.token};{datetime.strftime(self.lastLogin,Main.FORMAT_STR)}\n"

class Main:
    RECENT_ACC_PATH = "recent_accs.csv"
    FORMAT_STR = "%Y-%m-%dT%H:%M:%S.%fZ"
    
    accounts: dict[str,Account]
    active_acc: Account
    selected_ship:str

    st: SpaceTraders

    
    #region bools
    _is_logged_in=False
    _is_logged_in=False
    #endregion
    # region timestamps
    _ships_update:datetime=None
    _agent_update:datetime=None
    _contracts_update:datetime=None
    _systems_update:datetime=None
    # endregion


    def __init__(self) -> None:
        self.accounts = {}
        # state welcher acc
        # recent acc list
        # kopfzeile
        self.selected_ship=""

    def load_recent(self):
        with open(Main.RECENT_ACC_PATH, "r") as f:
            lines = f.readlines()
            for line in lines:
                name, token, lastLogin = line.replace("\n","").split(";")
                acc = Account(name, token, datetime.strptime(lastLogin,Main.FORMAT_STR))
                self.accounts[acc.name]=acc
            

    def get_recent(self) -> Account | None:
        if len(self.accounts) == 0:
            return None
        return max(self.accounts.values(),key=lambda acc : acc.lastLogin)

    def set_active(self, acc: Account):
        acc.lastLogin = datetime.utcnow()
        self.accounts[acc.name]=acc
        self.active_acc = acc
        self.save_accounts()

    def login(self, token):
        self.st = SpaceTraders(token)
        agent = self.st.get_agent()
        if not agent:
            return False
        name = agent.symbol
        acc = self.accounts.get(name) or Account(name,token,datetime.utcnow())
        self.set_active(acc)
        print(f"Logged into {name}")
        self._is_logged_in=True
        # pprint(self.st.agent)
        return True

    def is_logged_in(self):
        return self._is_logged_in

    def register(self, name, faction):
        raise NotImplementedError()

    def save_accounts(self):
        with open(Main.RECENT_ACC_PATH,"w") as f:
            for acc in self.accounts.values():
                f.write(acc.toCSV())

    def select_ship(self,ship):
        self.selected_ship=ship

    def get_systems(self):
        
        now = datetime.utcnow()
        if not self._systems_update or (now-self._systems_update).total_seconds()>60:
            self.st.get_systems()
            self._systems_update=now
        return self.st.systems

    def get_systems_plot(self):
        systems = self.get_systems()
        plt.figure(facecolor=((13/255,52/255,70/255)))
        ax = plt.axes()
        ax.set_facecolor((20/255,58/255,80/255))
        plt.plot([s.x for s in systems],[s.y for s in systems],marker=".",markersize=1,linestyle = "None")
        plt.subplots_adjust(.1,.1,.9,.9)
        return plt.gcf()
    def get_system_plot(self,system):
        waypoints = self.st.get_system_waypoints(system)
        plt.figure(facecolor=((13/255,52/255,70/255)))
        ax = plt.axes()
        ax.set_facecolor((20/255,58/255,80/255))
        plt.plot([s.x for s in waypoints],[s.y for s in waypoints],marker=".",markersize=3,linestyle = "None")
        plt.subplots_adjust(.1,.1,.9,.9)
        return plt.gcf()

    def get_agent(self):
        now = datetime.utcnow()
        if not self._agent_update or (now-self._agent_update).total_seconds()>60:
            self.st.get_agent()
            self._agent_update=now
        return self.st.agent

    def get_ships(self):
        now = datetime.utcnow()
        if not self._ships_update or (now-self._ships_update).total_seconds()>60:
            self.st.get_my_ships()
            self._ships_update=now
        return self.st.ships

    def get_contracts(self):
        now = datetime.utcnow()
        if not self._contracts_update or (now-self._contracts_update).total_seconds()>60:
            self.st.get_contracts()
            self._contracts_update=now
        return self.st.contracts
    
    def dock_ship(self,shipName):
        self.st.dock_ship(shipName)
    def orbit_ship(self,shipName):
        self.st.orbit_ship(shipName)
    def get_waypoints(self,system):
        return self.st.get_system_waypoints(system)
    def navigate_ship(self,ship,waypoint):
        if self.st.ships[ship].nav.waypointSymbol==waypoint:
            return True
        return self.st.navigate_ship(ship,waypoint)
    def sell_good(self,ship,good,units):
        return self.st.sell_cargo(ship,good,units)
    def jettison_good(self,ship,good,units):
        return self.st.jettison(ship,good,units)
    def refuel(self,ship):
        return self.st.refuel_ship(ship)
    def excavate(self,ship,survey=None):
        return self.st.extract_resources(ship,survey)
    def survey(self,ship):
        return self.st.create_survey(ship)
    def get_cooldown(self,ship):
        return self.st.cooldowns[ship] if ship in self.st.cooldowns else self.st.get_ship_cooldown(ship)

    def get_surveys(self):
        return self.st.surveys
    def remove_survey(self,id):
        return self.st.remove_survey(id)

    def get_time_diff(self,big,small):
        return (big-small).total_seconds()
    def parse_time(self,tstr):
        return datetime.strptime(tstr,Main.FORMAT_STR)

if __name__ == "__main__":
    m = Main()
    m.load_recent()
    pprint([(a.name,a.lastLogin) for a in m.accounts.values()])

    print()
