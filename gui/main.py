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

    st: SpaceTraders

    def __init__(self) -> None:
        self.accounts = {}
        # state welcher acc
        # recent acc list
        # kopfzeile

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
        acc.lastLogin = datetime.now()
        self.accounts[acc.name]=acc
        self.active_acc = acc
        self.save_accounts()

    def login(self, token):
        self.st = SpaceTraders(token)
        agent = self.st.get_agent()
        if not agent:
            return False
        name = agent.symbol
        acc = self.accounts.get(name) or Account(name,token,datetime.now())
        self.set_active(acc)
        print(f"Logged into {name}")
        return True

    def register(self, name, faction):
        raise NotImplementedError()

    def save_accounts(self):
        with open(Main.RECENT_ACC_PATH,"w") as f:
            for acc in self.accounts.values():
                f.write(acc.toCSV())



    def get_systems_plot(self):
        systems = self.st.get_systems()
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


if __name__ == "__main__":
    m = Main()
    pprint(m.accounts)

    print("hallo")
