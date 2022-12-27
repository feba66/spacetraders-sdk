from dataclasses import dataclass
from datetime import datetime
from pprint import pprint
import time
import PySimpleGUI as sg
import os
import sys

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


if __name__ == "__main__":
    m = Main()
    pprint(m.accounts)

    print("hallo")
