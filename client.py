
import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
from openapi_client.models import *

from api import SpaceTraders
import PySimpleGUI as sg

st = SpaceTraders()
agent = st.get_agent().body["data"]
credits = agent["credits"]
ships = st.get_my_ships().body["data"]

sg.theme("dark")

agent_info = [[sg.Text(agent["symbol"])], [sg.Text("Credits: "+str(credits))]]
ship_infos = []
print()
for s in ships:
    for l in s:
        print(l + ": "+str(s[l]))
        print()
    #,sg.ProgressBar(s["crew"]["capacity"],"h",(20,20),key="-crewBar-")
    ship_infos.append([sg.Frame(s["symbol"]+" "+s["registration"]["role"], [
        [sg.Text("nav: "+s["nav"]["status"]+"\n- Location: "+s["nav"]["waypointSymbol"]+"\n- Mode: "+s["nav"]["flightMode"])],
        [sg.Text("crew: "+str(s["crew"]["current"])+"/"+str(s["crew"]["capacity"])+" \nreq: "+str(s["crew"]["required"])
            +"\n- Rotation: "+str(s["crew"]["rotation"])+"\n- Morale: "+str(s["crew"]["morale"])+"\n- Wages: "+str(s["crew"]["wages"]))] if s["crew"]["capacity"] >0 else [],
        [sg.Text("Fuel: "+str(s["fuel"]["current"])+"/"+str(s["fuel"]["capacity"]))],
        [sg.Text("Frame: "+str(s["frame"]["name"])+"")]
        ])
    ])
layout = [[sg.Frame("Agent", agent_info)], [sg.Frame("Ships", ship_infos)], [sg.Button("OK")]]
window = sg.Window(title="Main Window", layout=layout, margins=(10, 10))
window.read(0)
# window.find_element("-crewBar-").update_bar(s["crew"]["current"])

while True:
    # window["-crewBar-"].update_bar(s["crew"]["current"])

    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

window.close()
