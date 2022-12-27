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


class Main:
    accounts: dict[str,Account]
    active_acc: Account

    st: SpaceTraders

    def __init__(self) -> None:
        self.accounts = {}
        # state welcher acc
        # recent acc list
        # kopfzeile

    def load_recent(self, path: str):
        with open(path, "r") as f:
            try:
                name, token, lastLogin = f.readline().split(";")
                acc = Account(name, token, datetime.strptime(lastLogin))
                self.accounts[acc.name]=acc
            except:
                pass

    @property
    def get_recent(self):
        return max([self.accounts[accname].lastLogin for accname in self.accounts])

    def set_active(self, acc: Account):
        acc.lastLogin = datetime.now()
        self.accounts[acc.name]=acc
        self.active_acc = acc

    def login(self, token):
        self.st = SpaceTraders(token)
        name = self.st.get_agent().symbol
        acc = self.accounts.get(name) or Account(name,token,datetime.now())
        self.set_active(acc)
        print(f"Logged into {name}")

    def register(self, name, faction):
        raise NotImplementedError()
        


if __name__ == "__main__":
    m = Main()
    pprint(m.accounts)

    print("hallo")
