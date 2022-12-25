
import time
from typing import Optional
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
# from openapi_client.models import *
from dataclasses import dataclass
from enum import Enum


class ErrorCodes(Enum):
    WAYPOINT_ALREADY_CHARTED = 4230
@dataclass
class ShipRequirements():
    power:int
    crew:int
    slots:int
@dataclass
class ShipEngine():
    symbol: str
    requirements: ShipRequirements
    name:str
    description:str
    speed: int
    condition: int
@dataclass
class ShipReactor():
    symbol:str
    requirements: ShipRequirements
    name:str
    description:str
    powerOutput:str
    condition:int
@dataclass
class Consumed():
    amount: int
    timestamp: str
@dataclass
class ShipFuel():
    current: int
    capacity: int
    consumed: Consumed
@dataclass
class ShipCargoItem:
    symbol:str
    name:str
    description:str
    units:int
@dataclass
class ShipModule:
    symbol:str
    requirements:ShipRequirements
    name:str
    capacity:Optional[int]
    range:Optional[int]
    description:Optional[str]
@dataclass
class ShipMount:
    symbol:str
    requirements:ShipRequirements
    name:str
    description:Optional[str]
    strength:Optional[int]
@dataclass
class ShipCargo:
    units: int
    inventory: list[ShipCargoItem]
    capacity: int
@dataclass
class ShipFrame:
    symbol:str
    moduleSlots:int
    requirements:ShipRequirements
    fuelCapacity:int
    name:str
    description:str
    mountingPoints:int
    condition:Optional[int]
@dataclass
class ShipCrew:
    # The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.
    wages:int
    current:int
    rotation:str
    morale:int
    required:int
    capacity:int
@dataclass
class ShipRegistration:
    role:str
    name:str
    factionSymbol:Optional[str]
@dataclass
class ShipNavRouteWaypoint:
    symbol:str
    systemSymbol:str
    x:int
    y:int
    type:str
@dataclass
class ShipNavRoute:
    arrival:str
    destination:ShipNavRouteWaypoint
    departure:ShipNavRouteWaypoint
class ShipNavFlightMode(Enum):
    DRIFT="DRIFT"
    STEALTH="STEALTH"
    CRUISE="CRUISE"
    BURN="BURN"
class ShipNavStatus(Enum):
    IN_TRANSIT="IN_TRANSIT"
    IN_ORBIT="IN_ORBIT"
    DOCKED="DOCKED"
@dataclass
class ShipNav:
    route: ShipNavRoute
    systemSymbol:str
    waypointsSymbol:str
    flightMode:ShipNavFlightMode
    status:ShipNavStatus
@dataclass
class Ship():
    nav: ShipNav
    engine: ShipEngine
    fuel: ShipFuel
    reactor: ShipReactor
    mounts: list[ShipMount]
    registration: ShipRegistration
    cargo: ShipCargo
    modules: list[ShipModule]
    crew: ShipCrew
    frame: ShipFrame
class SystemType(Enum):
    NEUTRON_STAR="NEUTRON_STAR"
    RED_STAR="RED_STAR"
    ORANGE_STAR="ORANGE_STAR"
    BLUE_STAR="BLUE_STAR"
    YOUNG_STAR="YOUNG_STAR"
    WHITE_DWARF="WHITE_DWARF"
    BLACK_HOLE="BLACK_HOLE"
    HYPERGIANT="HYPERGIANT"
    NEBULA="NEBULA"
    UNSTABLE="UNSTABLE"
class WaypointType(Enum):
    PLANET="PLANET"
    GAS_GIANT="GAS_GIANT"
    MOON="MOON"
    ORBITAL_STATION="ORBITAL_STATION"
    JUMP_GATE="JUMP_GATE"
    ASTEROID_FIELD="ASTEROID_FIELD"
    NEBULA="NEBULA"
    DEBRIS_FIELD="DEBRIS_FIELD"
    GRAVITY_WELL="GRAVITY_WELL"
@dataclass
class SystemWaypoint:
    symbol:str
    x:int
    y:int
    type:WaypointType

    def __init__(self,symbol,x=None,y=None,type=None) -> None:
        if x == None or y == None or type== None:
            self.__init__(symbol["symbol"],symbol["x"],symbol["y"],symbol["type"])
        else:
            self.symbol=symbol
            self.x=x.as_int_oapg
            self.y=y.as_int_oapg
            self.type = WaypointType[type] if not isinstance(type,WaypointType) else type
    def __str__(self) -> str:
        return f"Waypoint({self.symbol}, ({self.x}|{self.y}), {self.type.name})"
    def __repr__(self) -> str:
        return self.__str__()
@dataclass
class System:
    symbol:str
    sectorSymbol:str
    x:int
    y:int
    type: SystemType
    waypoints: list[SystemWaypoint]
    factions: list[str]

    def __init__(self,symbol,sectorSymbol=None,x=None,y=None,type=None,waypoints=None,factions=None) -> None:
        if sectorSymbol==None or x==None or y == None or type==None or waypoints==None or factions == None:
            self.__init__(symbol["symbol"],symbol["sectorSymbol"],symbol["x"],symbol["y"],symbol["type"],symbol["waypoints"],symbol["factions"])
        else:
            self.symbol=symbol
            self.sectorSymbol=sectorSymbol
            self.x=x.as_int_oapg
            self.y=y.as_int_oapg
            self.type=SystemType[type] if not isinstance(type,SystemType) else type
            self.waypoints=[SystemWaypoint(w) for w in waypoints]
            self.factions=factions
    def __str__(self) -> str:
        return f"System({self.symbol}, {self.sectorSymbol}, ({self.x}|{self.y}), {self.type.name}, {self.waypoints}, {self.factions})"
    def __repr__(self) -> str:
        return self.__str__()
class WaypointTraitSymbols(Enum):
    UNCHARTED="UNCHARTED"
    MARKETPLACE="MARKETPLACE"
    SHIPYARD="SHIPYARD"
    OUTPOST="OUTPOST"
    SCATTERED_SETTLEMENTS="SCATTERED_SETTLEMENTS"
    SPRAWLING_CITIES="SPRAWLING_CITIES"
    MEGA_STRUCTURES="MEGA_STRUCTURES"
    OVERCROWDED="OVERCROWDED"
    HIGH_TECH="HIGH_TECH"
    CORRUPT="CORRUPT"
    BUREAUCRATIC="BUREAUCRATIC"
    TRADING_HUB="TRADING_HUB"
    INDUSTRIAL="INDUSTRIAL"
    BLACK_MARKET="BLACK_MARKET"
    RESEARCH_FACILITY="RESEARCH_FACILITY"
    MILITARY_BASE="MILITARY_BASE"
    SURVEILLANCE_OUTPOST="SURVEILLANCE_OUTPOST"
    EXPLORATION_OUTPOST="EXPLORATION_OUTPOST"
    MINERAL_DEPOSITS="MINERAL_DEPOSITS"
    COMMON_METAL_DEPOSITS="COMMON_METAL_DEPOSITS"
    PRECIOUS_METAL_DEPOSITS="PRECIOUS_METAL_DEPOSITS"
    RARE_METAL_DEPOSITS="RARE_METAL_DEPOSITS"
    METHANE_POOLS="METHANE_POOLS"
    ICE_CRYSTALS="ICE_CRYSTALS"
    EXPLOSIVE_GASES="EXPLOSIVE_GASES"
    STRONG_MAGNETOSPHERE="STRONG_MAGNETOSPHERE"
    VIBRANT_AURORAS="VIBRANT_AURORAS"
    SALT_FLATS="SALT_FLATS"
    CANYONS="CANYONS"
    PERPETUAL_DAYLIGHT="PERPETUAL_DAYLIGHT"
    PERPETUAL_OVERCAST="PERPETUAL_OVERCAST"
    DRY_SEABEDS="DRY_SEABEDS"
    MAGMA_SEAS="MAGMA_SEAS"
    SUPERVOLCANOES="SUPERVOLCANOES"
    ASH_CLOUDS="ASH_CLOUDS"
    VAST_RUINS="VAST_RUINS"
    MUTATED_FLORA="MUTATED_FLORA"
    TERRAFORMED="TERRAFORMED"
    EXTREME_TEMPERATURES="EXTREME_TEMPERATURES"
    EXTREME_PRESSURE="EXTREME_PRESSURE"
    DIVERSE_LIFE="DIVERSE_LIFE"
    SCARCE_LIFE="SCARCE_LIFE"
    FOSSILS="FOSSILS"
    WEAK_GRAVITY="WEAK_GRAVITY"
    STRONG_GRAVITY="STRONG_GRAVITY"
    CRUSHING_GRAVITY="CRUSHING_GRAVITY"
    TOXIC_ATMOSPHERE="TOXIC_ATMOSPHERE"
    CORROSIVE_ATMOSPHERE="CORROSIVE_ATMOSPHERE"
    BREATHABLE_ATMOSPHERE="BREATHABLE_ATMOSPHERE"
    JOVIAN="JOVIAN"
    ROCKY="ROCKY"
    VOLCANIC="VOLCANIC"
    FROZEN="FROZEN"
    SWAMP="SWAMP"
    BARREN="BARREN"
    TEMPERATE="TEMPERATE"
    JUNGLE="JUNGLE"
    OCEAN="OCEAN"
@dataclass
class WaypointTrait:
    symbol:WaypointTraitSymbols
    name:str
    description:str
    def __init__(self,symbol,name=None,description=None) -> None:
        if name == None or description==None:
            self.__init__(symbol["symbol"],symbol["name"],symbol["description"])
        else:
            self.symbol=WaypointTraitSymbols[symbol]
            self.name=name
            self.description=description
@dataclass
class WaypointFaction:
    symbol:str
@dataclass
class Chart:
    submittedBy:Optional[str]
    submittedOn:Optional[str]
@dataclass
class WaypointOrbital:
    symbol:str
@dataclass
class Waypoint:
    symbol:str
    traits:list[WaypointTrait]
    systemSymbol:str
    x:int
    y:int
    type:WaypointType
    orbitals:list[WaypointOrbital]
    faction:Optional[WaypointFaction]
    chart:Optional[Chart]

    def __init__(self,symbol,traits=None,systemSymbol=None,x=None,y=None,type=None,orbitals=None,faction=None,chart=None) -> None:
        if traits == None:
            self.__init__(symbol["symbol"],symbol["traits"],symbol["systemSymbol"],symbol["x"],symbol["y"],symbol["type"],symbol["orbitals"],symbol["faction"] if "faction" in symbol else None,symbol["chart"] if "chart" in symbol else None)
        else:
            self.symbol=symbol
            self.traits=[WaypointTrait(wt) for wt in traits]
            self.systemSymbol=systemSymbol
            self.x=x.as_int_oapg
            self.y=y.as_int_oapg
            self.type=WaypointType[type] if isinstance(type,WaypointType) else type
            self.orbitals=[WaypointOrbital(wo) for wo in orbitals]
            self.faction=faction
            self.chart=chart

@dataclass
class Market:
    symbol:str
    imports:list[str]
    exports:list[str]
    transactions:Optional[list]
    tradeGoods:Optional[list]
    def __init__(self,symbol,imports=None,exports=None,transactions=None,tradeGoods=None) -> None:
        pass

class SpaceTraders:

    api_client: openapi_client.ApiClient

    api_agents = agents_api.AgentsApi
    api_contracts = contracts_api.ContractsApi
    def_api = default_api.DefaultApi
    api_factions = factions_api.FactionsApi
    api_fleet = fleet_api.FleetApi
    api_systems: systems_api.SystemsApi

    systems: list[System]

    def __init__(self) -> None:

        configuration = openapi_client.Configuration()
        with open("acc.txt", "r") as f:
            configuration.access_token = f.readline().replace("\n", "")
        self.api_client = openapi_client.ApiClient(configuration)

        self.api_agents = agents_api.AgentsApi(self.api_client)
        self.api_contracts = contracts_api.ContractsApi(self.api_client)
        self.def_api = default_api.DefaultApi(self.api_client)
        self.api_factions = factions_api.FactionsApi(self.api_client)
        self.api_fleet = fleet_api.FleetApi(self.api_client)
        self.api_systems = systems_api.SystemsApi(self.api_client)

    def register(self):
        # Create an instance of the API class
        try:
            r = self.def_api.register(body={"symbol": "febat3st", "faction": "ASTRO"})
            pprint(r.body)
            pprint(r.response.data)
            return r
        except openapi_client.ApiException as e:
            pprint(e)

    # region AgentsApi
    def get_agent(self):
        try:
            api_response = self.api_agents.get_my_agent()
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
    # endregion
    # region ContactsApi

    def accept_contract(self, contractId):
        try:
            api_response = self.api_contracts.accept_contract(
                path_params={"contractId": contractId})
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->accept_contract: %s\n" % e)

    def deliver_contract(self, contractId, tradeSymbol, shipSymbol, units):
        try:
            api_response = self.api_contracts.deliver_contract(path_params={"contractId": contractId}, body={
                                                               "tradeSymbol": tradeSymbol, "shipSymbol": shipSymbol, "units": units})
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->deliver_contract: %s\n" % e)

    def get_contracts(self):

        try:
            api_response = self.api_contracts.get_contracts()
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    # endregion
    # region FleetApi

    def chart(self, shipSymbol):
        try:
            api_response = self.api_fleet.create_chart(path_params={"shipSymbol": shipSymbol})
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)

    def purchase_ship(self, waypointSymbol,shipType):
        try:
            api_response = self.api_fleet.purchase_ship(body={"waypointSymbol": waypointSymbol,"shipType":shipType})
            # pprint(api_response)
            return api_response.body["data"]
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    def get_my_ships(self):
        try:
            api_response = self.api_fleet.get_my_ships()
            print()
            for k in api_response.body["data"]:
                print(k)
                for l in k:
                    print(l)
                print()
            pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    # endregion
    # region SystemsApi
    def get_systems(self) -> list[System]:#done
        """Gets all systems
        :return: A list of all Systems
        """
        try:
            r = self.api_systems.get_systems()
            systems = []
            for s in r.body["data"]:
                system = System(s)
                systems.append(system)
            self.systems = systems
            return systems
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_systems: %s\n" % e)
    def get_system(self,systemSymbol):#done
        """Gets the system information 
        :param systemSymbol: System name
        :return: the system object
        """
        try:
            s = self.api_systems.get_system(path_params={"systemSymbol": systemSymbol}).body["data"]
            return System(s)
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_system: %s\n" % e)
    
    def get_market(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_market(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol}).body["data"]
            # pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_market: %s\n" % e)
    def get_waypoint(self,systemSymbol,waypointSymbol):
        try:
            wa = self.api_systems.get_waypoint(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol}).body["data"]
            # pprint(api_response)
            return Waypoint(wa)
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    def get_shipyard(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_shipyard(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            # pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    # endregion


if __name__ == "__main__":
    st = SpaceTraders()
    st.get_agent()
    # st.get_contracts()
    # contract = "clbw3quox000ss60ju7qe7a8b"
    # st.accept_contract(contract)
    # st.get_my_ships()
    ship = "FEBAT3ST-1"
    # st.chart(ship)
    system = "X1-PH88"
    shipyards = []
    markets=[]
    s = st.get_system(system)
    for wa in s.waypoints:
        w = st.get_waypoint(system,wa.symbol)
        print(w.symbol)
        for t in w.traits:
            if t.symbol==WaypointTraitSymbols.SHIPYARD:
                shipyards.append(w.symbol)
            if t.symbol==WaypointTraitSymbols.MARKETPLACE:
                markets.append(w.symbol)
            print(" "+t.name)
    for shipyard in shipyards:
        print(shipyard)
        sy = st.get_shipyard(system,shipyard).body["data"]
        # print(sy)
        for t in sy["shipTypes"]:
            print(" "+t["type"])
    for market in markets:
        print(market)
        m = st.get_market(system,market)
        print(m)
    #         # ns = st.purchase_ship(shipyard,t["type"])
    #         # print(ns)
    # st.get_systems()
    # for s in st.systems:
    #     print(s)
    # st.get_my_ships()
