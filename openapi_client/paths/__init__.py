# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    REGISTER = "/register"
    SYSTEMS = "/systems"
    SYSTEMS_SYSTEM_SYMBOL = "/systems/{systemSymbol}"
    SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS = "/systems/{systemSymbol}/waypoints"
    SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL = "/systems/{systemSymbol}/waypoints/{waypointSymbol}"
    SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_MARKET = "/systems/{systemSymbol}/waypoints/{waypointSymbol}/market"
    SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_SHIPYARD = "/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard"
    FACTIONS = "/factions"
    FACTIONS_FACTION_SYMBOL = "/factions/{factionSymbol}"
    MY_AGENT = "/my/agent"
    MY_CONTRACTS = "/my/contracts"
    MY_CONTRACTS_CONTRACT_ID = "/my/contracts/{contractId}"
    MY_CONTRACTS_CONTRACT_ID_ACCEPT = "/my/contracts/{contractId}/accept"
    MY_CONTRACTS_CONTRACT_ID_DELIVER = "/my/contracts/{contractId}/deliver"
    MY_CONTRACTS_CONTRACT_ID_FULFILL = "/my/contracts/{contractId}/fulfill"
    MY_SHIPS_SHIP_SYMBOL_ORBIT = "/my/ships/{shipSymbol}/orbit"
    MY_SHIPS = "/my/ships"
    MY_SHIPS_SHIP_SYMBOL = "/my/ships/{shipSymbol}"
    MY_SHIPS_SHIP_SYMBOL_CHART = "/my/ships/{shipSymbol}/chart"
    MY_SHIPS_SHIP_SYMBOL_COOLDOWN = "/my/ships/{shipSymbol}/cooldown"
    MY_SHIPS_SHIP_SYMBOL_DEPLOY = "/my/ships/{shipSymbol}/deploy"
    MY_SHIPS_SHIP_SYMBOL_DOCK = "/my/ships/{shipSymbol}/dock"
    MY_SHIPS_SHIP_SYMBOL_SURVEY = "/my/ships/{shipSymbol}/survey"
    MY_SHIPS_SHIP_SYMBOL_EXTRACT = "/my/ships/{shipSymbol}/extract"
    MY_SHIPS_SHIP_SYMBOL_JETTISON = "/my/ships/{shipSymbol}/jettison"
    MY_SHIPS_SHIP_SYMBOL_JUMP = "/my/ships/{shipSymbol}/jump"
    MY_SHIPS_SHIP_SYMBOL_NAVIGATE = "/my/ships/{shipSymbol}/navigate"
    MY_SHIPS_SHIP_SYMBOL_WARP = "/my/ships/{shipSymbol}/warp"
    MY_SHIPS_SHIP_SYMBOL_SELL = "/my/ships/{shipSymbol}/sell"
    MY_SHIPS_SHIP_SYMBOL_SCAN_SYSTEMS = "/my/ships/{shipSymbol}/scan/systems"
    MY_SHIPS_SHIP_SYMBOL_SCAN_SHIPS = "/my/ships/{shipSymbol}/scan/ships"
    MY_SHIPS_SHIP_SYMBOL_REFUEL = "/my/ships/{shipSymbol}/refuel"
    MY_SHIPS_SHIP_SYMBOL_PURCHASE = "/my/ships/{shipSymbol}/purchase"
    MY_SHIPS_SHIP_SYMBOL_TRANSFER = "/my/ships/{shipSymbol}/transfer"
