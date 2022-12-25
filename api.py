
import time
from typing import Optional
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
from dataclasses import dataclass
from enum import Enum

PATH_PREFIX = "spacetraders-sdk/"

# region Enums

class ErrorCodes(Enum):
    WAYPOINT_ALREADY_CHARTED = 4230

    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
class ContractType(Enum):
    PROCUREMENT="PROCUREMENT"
    TRANSPORT="TRANSPORT"
    SHUTTLE="SHUTTLE"

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
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
class ShipType(Enum):
    SHIP_PROBE="SHIP_PROBE"
    SHIP_MINING_DRONE="SHIP_MINING_DRONE"
    SHIP_INTERCEPTOR="SHIP_INTERCEPTOR"
    SHIP_LIGHT_HAULER="SHIP_LIGHT_HAULER"
    SHIP_COMMAND_FRIGATE="SHIP_COMMAND_FRIGATE"
    SHIP_EXPLORER="SHIP_EXPLORER"
    SHIP_HEAVY_FREIGHTER="SHIP_HEAVY_FREIGHTER"
    SHIP_LIGHT_SHUTTLE="SHIP_LIGHT_SHUTTLE"
    SHIP_ORE_HOUND="SHIP_ORE_HOUND"
    SHIP_REFINING_FREIGHTER="SHIP_REFINING_FREIGHTER"
    
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name
# endregion

# region Classes
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
class ShipRequirements:
    power:int
    crew:int
    slots:int
    def __init__(self,data) -> None:
        self.power=data["power"].as_int_oapg if "power" in data else None
        self.crew=data["crew"].as_int_oapg if "crew" in data else None
        self.slots=data["slots"].as_int_oapg if "slots" in data else None
@dataclass
class ShipEngine:
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
class ShipReactor:
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
class Consumed:
    amount: int
    timestamp: str
    def __init__(self,data) -> None:
        self.amount=data["amount"].as_int_oapg
        self.timestamp=data["timestamp"]
@dataclass
class ShipFuel:
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
class Ship:
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
@dataclass
class SystemWaypoint:
    symbol:str
    x:int
    y:int
    type:WaypointType
    
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.x=data["x"].as_int_oapg
        self.y=data["y"].as_int_oapg
        self.type=WaypointType[data["type"]]
@dataclass
class System:
    symbol:str
    sectorSymbol:str
    x:int
    y:int
    type: SystemType
    waypoints: list[SystemWaypoint]
    factions: list[str]

    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.sectorSymbol=data["sectorSymbol"]
        self.x=data["x"].as_int_oapg
        self.y=data["y"].as_int_oapg
        self.type=SystemType[data["type"]]
        self.waypoints=[SystemWaypoint(w) for w in data["waypoints"]]
        self.factions=[str(f) for f in data["factions"]]
@dataclass
class WaypointTrait:
    symbol:WaypointTraitSymbols
    name:str
    description:str
    def __init__(self,data) -> None:
            self.symbol=WaypointTraitSymbols[data["symbol"]]
            self.name=data["name"]
            self.description=data["description"]
    def __repr__(self) -> str:
        return "WaypointTrait(name='"+self.name+"', description='"+self.description+"')"
@dataclass
class WaypointFaction:
    symbol:str
    def __init__(self,data) -> None:
        self.symbol = data["symbol"]
@dataclass
class Chart:
    submittedBy:Optional[str]
    submittedOn:Optional[str]
    def __init__(self,data) -> None:
        self.submittedBy = data["submittedBy"] if "submittedBy" in data else None
        self.submittedOn = data["submittedOn"] if "submittedOn" in data else None
@dataclass
class WaypointOrbital:
    symbol:str
    def __init__(self,data) -> None:
        self.symbol = data["symbol"]
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

    def __init__(self,data) -> None:
        self.symbol = data["symbol"]
        self.traits = [WaypointTrait(t) for t in data["traits"]]
        self.systemSymbol = data["systemSymbol"]
        self.x = data["x"].as_int_oapg
        self.y = data["y"].as_int_oapg
        self.type = WaypointType[data["type"]]
        self.orbitals = [WaypointOrbital(o) for o in data["orbitals"]]
        self.faction = WaypointFaction(data["faction"]) if "faction" in data else None
        self.chart = Chart(data["chart"]) if "chart" in data else None
@dataclass
class ShipyardTransaction:
    price:int
    agentSymbol:str
    timestamp:str
    shipSymbol:Optional[str]
    def __init__(self,data) -> None:
        self.price = data["price"].as_int_oapg
        self.agentSymbol = data["agentSymbol"]
        self.timestamp = data["timestamp"]
        self.shipSymbol = data["shipSymbol"] if "shipSymbol" in data else None
@dataclass
class ShipyardShip:
    engine: ShipEngine
    reactor: ShipReactor
    name:str
    description:str
    mounts: list[ShipMount]
    purchasePrice: int
    modules: list[ShipModule]
    frame:ShipFrame
    type:Optional[ShipType]

    def __init__(self,data) -> None:
        self.engine=ShipEngine(data["engine"])
        self.reactor=ShipReactor(data["reactor"])
        self.name=data["name"]
        self.description=data["description"]
        self.mounts=[ShipMount(x) for x in data["mounts"]]
        self.purchasePrice = data["purchasePrice"]
        self.modules=[ShipModule(x) for x in data["modules"]]
        self.frame=ShipFrame(data["frame"])
        self.type = ShipType[data["type"]] if "type" in data else None 
@dataclass
class Shipyard:
    shipTypes: list[ShipType]
    symbol:str
    transactions:Optional[list[ShipyardTransaction]]
    ships:Optional[list[ShipyardShip]]
    def __init__(self,data) -> None:
        self.shipTypes=[ShipType[t["type"]] for t in data["shipTypes"]]
        self.symbol=data["symbol"]
        self.transactions=[ShipyardTransaction(t) for t in data["transactions"]] if "transactions" in data else None
        self.ships=[ShipyardShip(s) for s in data["ships"]] if "ships" in data else None

@dataclass
class Market:
    symbol:str
    imports:list[str]
    exports:list[str]
    transactions:Optional[list]
    tradeGoods:Optional[list]

# endregion

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
            with open(PATH_PREFIX+"acc.txt", "r") as f:
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
            with open(PATH_PREFIX+"acc.txt","a") as f:
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
            print("Exception when calling DefaultApi->register: %s\n" % e)
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
     # NOTE: cant find the route maybe its not implemented yet
    def get_factions(self):
        try:
            api_response = self.api_factions.get_factions()
            return [Faction(f) for f in api_response.body["data"]]
        except openapi_client.ApiException as e:
            print("Exception when calling FactionsApi->get_factions: %s\n" % e)
    def get_faction(self,factionSymbol):
        try:
            api_response = self.api_factions.get_faction(path_params={"factionSymbol": factionSymbol})
            return Faction(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling FactionsApi->get_faction: %s\n" % e)
    # endregion
    
    # region ContactsApi
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

    # endregion
    
    # region SystemsApi
    def get_waypoint(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_waypoint(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            return Waypoint(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_waypoint: %s\n" % e)


    def get_shipyard(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_shipyard(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            # pprint(api_response)
            return Shipyard(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_shipyard: %s\n" % e)
    def get_system_waypoints(self,systemSymbol):
        try:
            api_response = self.api_systems.get_system_waypoints(path_params={"systemSymbol": systemSymbol})
            return [Waypoint(w) for w in api_response.body["data"]]
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_system_waypoints: %s\n" % e)
    def get_system(self,systemSymbol):
        try:
            api_response = self.api_systems.get_system(path_params={"systemSymbol": systemSymbol})
            return System(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_system: %s\n" % e)
    def get_systems(self):
        try:
            api_response = self.api_systems.get_systems()
            with open(PATH_PREFIX+"systems.json","w") as f:
                f.write(str(api_response.response.data).replace("b'","").replace("'",""))
            self.systems = [System(s) for s in api_response.body["data"]]
            return self.systems
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_systems: %s\n" % e)
    # endregion

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


    
    
    
    def get_market(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_market(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol}).body["data"]
            # pprint(api_response)
            return api_response
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_market: %s\n" % e)
    

if __name__ == "__main__":
    st = SpaceTraders()

    # st.register("test0003","COSMIC")
    # pprint(st.get_factions())

    # exit()
    # pprint(st.get_agent())
    system = "X1-UV97"
    waypoint = "X1-UV97-21170Z"
    shipyardWaypoint = "X1-UV97-44217E"
    # pprint(st.get_waypoint(system,waypoint))
    # pprint(st.get_system(system))
    # pprint(st.get_systems())
    # pprint(st.get_system_waypoints(system))
    pprint(st.get_shipyard(system,shipyardWaypoint))
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
