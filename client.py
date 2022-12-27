
import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
from openapi_client.models import *

from api import SpaceTraders
import PySimpleGUI as sg

st = SpaceTraders()
agent = st.get_agent()
credits = agent.credits
ships = st.get_my_ships()

sg.theme("darkteal10")

# agent_info = [[sg.Text(agent.symbol)], [sg.Text("Credits: "+str(credits))]]
# ship_infos = []
# print()
# for s in ships:
#     #,sg.ProgressBar(s.crew.capacity,"h",(20,20),key="-crewBar-")
#     ship_infos.append([sg.Frame(s.symbol+" "+s.registration.role, [
#         [sg.Text("nav: "+str(s.nav.status)+"\n- Location: "+s.nav.waypointSymbol+"\n- Mode: "+str(s.nav.flightMode))],
#         [sg.Text("crew: "+str(s.crew.current)+"/"+str(s.crew.capacity)+" \nreq: "+str(s.crew.required)
#             +"\n- Rotation: "+str(s.crew.rotation)+"\n- Morale: "+str(s.crew.morale)+"\n- Wages: "+str(s.crew.wages))] if s.crew.capacity >0 else [],
#         [sg.Text("Fuel: "+str(s.fuel.current)+"/"+str(s.fuel.capacity))],
#         [sg.Text("Frame: "+str(s.frame.name)+"")]
#         ])
#     ])
# layout = [[sg.Frame("Agent", agent_info)], [sg.Frame("Ships", ship_infos)], [sg.Button("OK")]]
# window = sg.Window(title="Main Window", layout=layout, margins=(10, 10))
# window.read(0)
# window.find_element("-crewBar-").update_bar(s.crew.current)
register_layout = [[sg.Text("Name"), sg.InputText(key="-name-",size=(30, 10))], 
                   [sg.Text("Faction"), sg.DropDown( values=[x.symbol for x in st.get_factions()],key="-faction-", size=(27, 10))],
                   [sg.Button("Register"),sg.Button("To Login",k="-toLogin-")]]
login_layout = [[sg.Text("Token"), sg.InputText(size=(30, 10))],
                [sg.Button("Login"),sg.Button("To Register",k="-toRegister-")]]
# first_layout = [[sg.Frame("Register", register_layout)],
#           [sg.Frame("Login", login_layout)]]
# window = sg.Window(title="Space Traders Client", layout=[[sg.Column(register_layout,key="-l1-",visible=True)],[sg.Column(login_layout,key="-l2-",visible=False)]], margins=(10, 10))
window = sg.Window(title="Space Traders Client", layout=[[sg.pin(sg.Column(register_layout,key="-l1-",visible=True)),sg.pin(sg.Column(login_layout,key="-l2-",visible=False))]], margins=(10, 10))

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


"""
1. Login/register
register: textinput name
          dropdown faction
          checkbox keeploggedin
login: textinput token
        maybe dropdown with already saved tokens/usernames

db: table users
columns: username, token

"""
