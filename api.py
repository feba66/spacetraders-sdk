
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

    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name

@dataclass
class Agent:
    accountId:str
    symbol:str
    headquarters:str
    credits:int

    def __init__(self,data) -> None:
        self.accountId=data["accountId"]
        self.symbol=data["symbol"]
        self.headquarters=data["headquarters"]
        self.credits=data["credits"].as_int_oapg
class ContractType(Enum):
    PROCUREMENT="PROCUREMENT"
    TRANSPORT="TRANSPORT"
    SHUTTLE="SHUTTLE"

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
@dataclass
class ContractPayment:
    onFulfilled:int
    onAccepted:int
    def __init__(self,data) -> None:
        self.onFulfilled=data["onFulfilled"].as_int_oapg
        self.onAccepted=data["onAccepted"].as_int_oapg
@dataclass
class ContractDeliverGood:
    tradeSymbol:str
    unitsRequired:int
    destinationSymbol:str
    unitsFulfilled:int

    def __init__(self,data) -> None:
        self.tradeSymbol=data["tradeSymbol"]
        self.unitsRequired=data["unitsRequired"].as_int_oapg
        self.destinationSymbol=data["destinationSymbol"]
        self.unitsFulfilled=data["unitsFulfilled"].as_int_oapg
@dataclass
class ContractTerms:
    payment:ContractPayment
    deadline:str
    deliver:Optional[list[ContractDeliverGood]]
@dataclass
class Contract:
    terms:ContractTerms
    factionSymbol:str
    fulfilled:bool
    accepted:bool
    expiration:str
    id:str
    type:ContractType

    def __init__(self,data) -> None:
        self.terms = ContractTerms(ContractPayment(data["terms"]["payment"]),data["terms"]["deadline"],[ContractDeliverGood(d) for d in data["terms"]["deliver"]])
        self.id = data["id"]
        self.fulfilled = data["fulfilled"].is_true_oapg()
        self.accepted = data["accepted"].is_true_oapg()
        self.expiration = data["expiration"]
        self.factionSymbol = data["factionSymbol"]
        self.type = ContractType[data["type"]]
class FactionTraitSymbol(Enum):
    BUREAUCRATIC="BUREAUCRATIC"
    SECRETIVE="SECRETIVE"
    CAPITALISTIC="CAPITALISTIC"
    INDUSTRIOUS="INDUSTRIOUS"
    PEACEFUL="PEACEFUL"
    DISTRUSTFUL="DISTRUSTFUL"
    WELCOMING="WELCOMING"
    ANARCHIST="ANARCHIST"
    CONFLICTED="CONFLICTED"
    AUTHORITARIAN="AUTHORITARIAN"
    OLIGARCHICAL="OLIGARCHICAL"
    DYNASTIC="DYNASTIC"
    DEMOCRACTIC="DEMOCRACTIC"
    DECENTRALIZED="DECENTRALIZED"
    SMUGGLERS="SMUGGLERS"
    SCAVENGERS="SCAVENGERS"
    REBELLIOUS="REBELLIOUS"
    EXILES="EXILES"
    PIRATES="PIRATES"
    RAIDERS="RAIDERS"
    CLAN="CLAN"
    GUILD="GUILD"
    DOMINION="DOMINION"
    FRINGE="FRINGE"
    FORSAKEN="FORSAKEN"
    ISOLATED="ISOLATED"
    LOCALIZED="LOCALIZED"
    ESTABLISHED="ESTABLISHED"
    NOTABLE="NOTABLE"
    DOMINANT="DOMINANT"
    INESCAPABLE="INESCAPABLE"
    INNOVATIVE="INNOVATIVE"
    BOLD="LD"
    VISIONARY="VISIONARY"
    CURIOUS="CURIOUS"
    DARING="DARING"
    EXPLORATORY="EXPLORATORY"
    RESOURCEFUL="RESOURCEFUL"
    FLEXIBLE="FLEXIBLE"
    COOPERATIVE="COOPERATIVE"
    UNITED="UNITED"
    STRATEGIC="STRATEGIC"
    INTELLIGENT="INTELLIGENT"
    RESEARCH_FOCUSED="RESEARCH_FOCUSED"
    COLLABORATIVE="COLLABORATIVE"
    PROGRESSIVE="PROGRESSIVE"
    MILITARISTIC="MILITARISTIC"
    TECHNOLOGICALLY_ADVANCED="TECHNOLOGICALLY_ADVANCED"
    AGGRESSIVE="AGGRESSIVE"
    IMPERIALISTIC="IMPERIALISTIC"
    TREASURE_HUNTERS="TREASURE_HUNTERS"
    DEXTEROUS="DEXTEROUS"
    UNPREDICTABLE="UNPREDICTABLE"
    BRUTAL="BRUTAL"
    FLEETING="FLEETING"
    ADAPTABLE="ADAPTABLE"
    SELF_SUFFICIENT="SELF_SUFFICIENT"
    DEFENSIVE="DEFENSIVE"
    PROUD="PROUD"
    DIVERSE="DIVERSE"
    INDEPENDENT="INDEPENDENT"
    SELF_INTERESTED="SELF_INTERESTED"
    FRAGMENTED="FRAGMENTED"
    COMMERCIAL="COMMERCIAL"
    FREE_MARKETS="FREE_MARKETS"
    ENTREPRENEURIAL="ENTREPRENEURIAL"

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
@dataclass
class FactionTrait:
    symbol:FactionTraitSymbol
    name:str
    description:str
    def __init__(self,data) -> None:
        self.name=data["name"]
        self.description=data["description"]
        self.symbol = FactionTraitSymbol[data["symbol"]]
@dataclass
class Faction:
    symbol:str
    headquarters:str
    traits:list[FactionTrait]
    name:str
    description:str
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.headquarters=data["headquarters"]
        self.name=data["name"]
        self.description=data["description"]
        self.traits=[FactionTrait(t) for t in data["traits"]]
@dataclass
class ShipRequirements():
    power:int
    crew:int
    slots:int
    def __init__(self,data) -> None:
        self.power=data["power"].as_int_oapg if "power" in data else None
        self.crew=data["crew"].as_int_oapg if "crew" in data else None
        self.slots=data["slots"].as_int_oapg if "slots" in data else None
@dataclass
class ShipEngine():
    symbol: str
    requirements: ShipRequirements
    name:str
    description:str
    speed: int
    condition: int
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"]
        self.speed=data["speed"].as_int_oapg
        self.condition=data["condition"].as_int_oapg
@dataclass
class ShipReactor():
    symbol:str
    requirements: ShipRequirements
    name:str
    description:str
    powerOutput:str
    condition:int
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"]
        self.powerOutput=data["powerOutput"]
        self.condition=data["condition"].as_int_oapg
@dataclass
class Consumed():
    amount: int
    timestamp: str
    def __init__(self,data) -> None:
        self.amount=data["amount"].as_int_oapg
        self.timestamp=data["timestamp"]
@dataclass
class ShipFuel():
    current: int
    capacity: int
    consumed: Consumed
    def __init__(self,data) -> None:
        self.current=data["current"].as_int_oapg
        self.capacity=data["capacity"].as_int_oapg
        self.consumed=Consumed(data["consumed"])
@dataclass
class ShipCargoItem:
    symbol:str
    name:str
    description:str
    units:int
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.name=data["name"]
        self.description=data["description"]
        self.units=data["units"].as_int_oapg
@dataclass
class ShipModule:
    symbol:str
    requirements:ShipRequirements
    name:str
    capacity:Optional[int]
    range:Optional[int]
    description:Optional[str]
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.capacity=data["capacity"].as_int_oapg if "capacity" in data else None
        self.range=data["range"].as_int_oapg if "range" in data else None
        self.description=data["description"] if "description" in data else None
@dataclass
class ShipMount:
    symbol:str
    requirements:ShipRequirements
    name:str
    description:Optional[str]
    strength:Optional[int]
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"] if "description" in data else None
        self.strength=data["strength"] if "description" in data else None
@dataclass
class ShipCargo:
    units: int
    inventory: list[ShipCargoItem]
    capacity: int
    def __init__(self,data) -> None:
        self.units=data["units"].as_int_oapg
        self.inventory=[ShipCargoItem(x) for x in data["inventory"]]
        self.capacity=data["capacity"].as_int_oapg
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
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.moduleSlots=data["moduleSlots"].as_int_oapg
        self.requirements=ShipRequirements(data["requirements"])
        self.fuelCapacity=data["fuelCapacity"].as_int_oapg
        self.name=data["name"]
        self.description=data["description"]
        self.mountingPoints=data["mountingPoints"].as_int_oapg
        self.condition=data["condition"].as_int_oapg if "condition" in data else None
@dataclass
class ShipCrew:
    # The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.
    wages:int
    current:int
    rotation:str
    morale:int
    required:int
    capacity:int
    def __init__(self,data) -> None:
        self.wages=data["wages"].as_int_oapg
        self.current=data["current"].as_int_oapg
        self.rotation=data["rotation"]
        self.morale=data["morale"].as_int_oapg
        self.required=data["required"].as_int_oapg
        self.capacity=data["capacity"].as_int_oapg
@dataclass
class ShipRegistration:
    role:str
    name:str
    factionSymbol:Optional[str]
    def __init__(self,data) -> None:
        self.role=data["role"]
        self.name=data["name"]
        self.factionSymbol=data["factionSymbol"] if "factionSymbol" in data else None
@dataclass
class ShipNavRouteWaypoint:
    symbol:str
    systemSymbol:str
    x:int
    y:int
    type:str
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.systemSymbol=data["systemSymbol"]
        self.x=data["x"].as_int_oapg
        self.y=data["y"].as_int_oapg
        self.type=data["type"]
@dataclass
class ShipNavRoute:
    arrival:str
    destination:ShipNavRouteWaypoint
    departure:ShipNavRouteWaypoint
    def __init__(self,data) -> None:
        self.arrival = data["arrival"]
        self.destination = ShipNavRouteWaypoint(data["destination"])
        self.departure = ShipNavRouteWaypoint(data["departure"])
class ShipNavFlightMode(Enum):
    DRIFT="DRIFT"
    STEALTH="STEALTH"
    CRUISE="CRUISE"
    BURN="BURN"
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
class ShipNavStatus(Enum):
    IN_TRANSIT="IN_TRANSIT"
    IN_ORBIT="IN_ORBIT"
    DOCKED="DOCKED"
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
@dataclass
class ShipNav:
    route: ShipNavRoute
    systemSymbol:str
    waypointSymbol:str
    flightMode:ShipNavFlightMode
    status:ShipNavStatus

    def __init__(self,data) -> None:
        self.route=ShipNavRoute(data["route"])
        self.systemSymbol=data["systemSymbol"]
        self.waypointSymbol=data["waypointSymbol"]
        self.flightMode=ShipNavFlightMode[data["flightMode"]]
        self.status=ShipNavStatus[data["status"]]
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

    def __init__(self,data) -> None:
        self.nav=ShipNav(data["nav"])
        self.engine=ShipEngine(data["engine"])
        self.fuel=ShipFuel(data["fuel"])
        self.reactor=ShipReactor(data["reactor"])
        self.registration=ShipRegistration(data["registration"])
        self.cargo=ShipCargo(data["cargo"])
        self.crew=ShipCrew(data["crew"])
        self.frame=ShipFrame(data["frame"])
        self.mounts=[ShipMount(x) for x in data["mounts"]]
        self.modules=[ShipModule(x) for x in data["modules"]]

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
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
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
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
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
    STRIPPED="STRIPPED"
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
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
    agent:Agent

    def __init__(self) -> None:

        configuration = openapi_client.Configuration()
        try:
            with open("spacetraders-sdk/acc.txt", "r") as f:
                configuration.access_token = f.readline().replace("\n", "")
        except:
            pass
        self.api_client = openapi_client.ApiClient(configuration)

        self.api_agents = agents_api.AgentsApi(self.api_client)
        self.api_contracts = contracts_api.ContractsApi(self.api_client)
        self.def_api = default_api.DefaultApi(self.api_client)
        self.api_factions = factions_api.FactionsApi(self.api_client)
        self.api_fleet = fleet_api.FleetApi(self.api_client)
        self.api_systems = systems_api.SystemsApi(self.api_client)

    # region DefaultApi
    def register(self,name,faction):
        try:
            r = self.def_api.register(body={"symbol": name, "faction": faction})

            token = r.body["data"]["token"]
            print(token)
            with open("spacetraders-sdk/acc.txt","a") as f:
                f.write(token+"\n")

            agent = Agent(r.body["data"]["agent"])
            contract = Contract(r.body["data"]["contract"])
            factionc = Faction(r.body["data"]["faction"])
            ship = Ship(r.body["data"]["ship"])
            pprint(agent)
            pprint(contract)
            pprint(factionc)
            pprint(ship)
            # pprint(r.response.data)
            return r
        except openapi_client.ApiException as e:
            pprint(e)
    # endregion
    # region AgentsApi
    def get_agent(self):
        try:
            api_response = self.api_agents.get_my_agent()
            agent = Agent(api_response.body["data"])
            self.agent = agent
            return  agent
        except openapi_client.ApiException as e:
            print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
    # endregion
    # region FactionsApi
    def get_factions(self):
        try:
            api_response = self.api_factions.get_factions()
            return [Faction(f) for f in api_response.body["data"]]
        except openapi_client.ApiException as e:
            print("Exception when calling FactionsApi->get_factions: %s\n" % e)
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

    def get_contract(self,contractId):
        try:
            api_response = self.api_contracts.get_contract(path_params = {"contractId": contractId})
            return Contract(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contract: %s\n" % e)
    def get_contracts(self):
        try:
            api_response = self.api_contracts.get_contracts()
            return [Contract(c) for c in api_response.body["data"]]
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
    def get_systems(self) -> list[System]:
        """Gets all systems
        :return: A list of all Systems
        """
        try:
            r = self.api_systems.get_systems()
            systems = []
            with open("systems.json","w") as f:
                f.write(str(r.response.data))
            print(r.body["meta"])
            for s in r.body["data"]:
                system = System(s)
                systems.append(system)
            self.systems = systems
            return systems
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_systems: %s\n" % e)
    def get_system(self,systemSymbol):
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

    # st.register("test0003","COSMIC")
    pprint(st.get_factions())

    # exit()
    # pprint(st.get_agent())

    # pprint(st.get_contract("clc3oyf4l000ss60j6lzyx2mv"))
    exit()
    # contract = "clbw3quox000ss60ju7qe7a8b"
    # st.accept_contract(contract)
    # st.get_my_ships()
    # ship = "FEBAT3ST-1"
    # st.chart(ship)
    system = "X1-UV97"
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
    print("== Shipyards ==")
    for shipyard in shipyards:
        print(shipyard)
        sy = st.get_shipyard(system,shipyard).body["data"]
        # print(sy)
        for t in sy["shipTypes"]:
            print(" "+t["type"])
    print("== Markets ==")
    for market in markets:
        print(market)
        m = st.get_market(system,market)
        print(m)
            # ns = st.purchase_ship(shipyard,t["type"])
            # print(ns)
    # st.get_systems()
    # for s in st.systems:
    #     print(s)
    # st.get_my_ships()
