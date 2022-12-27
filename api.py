
from datetime import datetime
import time
from typing import Optional
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
from dataclasses import dataclass
from enum import Enum

PATH_PREFIX = "spacetraders-sdk/"

# region Enums
class myEnum(Enum): 
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return self.name

class ErrorCodes(myEnum):
    WAYPOINT_ALREADY_CHARTED = 4230
    SURVEY_MUST_BE_DONE_WHILE_ORBITING = 4223
    INSUFFICIENT_FUNDS = 4216 #Failed to purchase ship. Agent has insufficient funds.
    ALREADY_ACCEPTED_CONTRACT = 4501
class ContractType(myEnum):
    PROCUREMENT="PROCUREMENT"
    TRANSPORT="TRANSPORT"
    SHUTTLE="SHUTTLE"
class FactionTraitSymbol(myEnum):
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
class ShipNavFlightMode(myEnum):
    DRIFT="DRIFT"
    STEALTH="STEALTH"
    CRUISE="CRUISE"
    BURN="BURN"
class ShipNavStatus(myEnum):
    IN_TRANSIT="IN_TRANSIT"
    IN_ORBIT="IN_ORBIT"
    DOCKED="DOCKED"
class SystemType(myEnum):
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
class WaypointType(myEnum):
    PLANET="PLANET"
    GAS_GIANT="GAS_GIANT"
    MOON="MOON"
    ORBITAL_STATION="ORBITAL_STATION"
    JUMP_GATE="JUMP_GATE"
    ASTEROID_FIELD="ASTEROID_FIELD"
    NEBULA="NEBULA"
    DEBRIS_FIELD="DEBRIS_FIELD"
    GRAVITY_WELL="GRAVITY_WELL"
class WaypointTraitSymbols(myEnum):
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
class ShipType(myEnum):
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
class TradeSymbol(myEnum):
    PRECIOUS_STONES="PRECIOUS_STONES"
    QUARTZ_SAND="QUARTZ_SAND"
    SILICON_CRYSTALS="SILICON_CRYSTALS"
    AMMONIA_ICE="AMMONIA_ICE"
    LIQUID_HYDROGEN="LIQUID_HYDROGEN"
    LIQUID_NITROGEN="LIQUID_NITROGEN"
    ICE_WATER="ICE_WATER"
    EXOTIC_MATTER="EXOTIC_MATTER"
    ADVANCED_CIRCUITRY="ADVANCED_CIRCUITRY"
    GRAVITON_EMITTERS="GRAVITON_EMITTERS"
    IRON="IRON"
    IRON_ORE="IRON_ORE"
    COPPER="COPPER"
    COPPER_ORE="COPPER_ORE"
    ALUMINUM="ALUMINUM"
    ALUMINUM_ORE="ALUMINUM_ORE"
    SILVER="SILVER"
    SILVER_ORE="SILVER_ORE"
    GOLD="GOLD"
    GOLD_ORE="GOLD_ORE"
    PLATINUM="PLATINUM"
    PLATINUM_ORE="PLATINUM_ORE"
    DIAMONDS="DIAMONDS"
    URANITE="URANITE"
    URANITE_ORE="URANITE_ORE"
    MERITIUM="MERITIUM"
    MERITIUM_ORE="MERITIUM_ORE"
    HYDROCARBON="HYDROCARBON"
    ANTIMATTER="ANTIMATTER"
    FERTILIZERS="FERTILIZERS"
    FABRICS="FABRICS"
    FOOD="FOOD"
    JEWELRY="JEWELRY"
    MACHINERY="MACHINERY"
    FIREARMS="FIREARMS"
    ASSAULT_RIFLES="ASSAULT_RIFLES"
    MILITARY_EQUIPMENT="MILITARY_EQUIPMENT"
    EXPLOSIVES="EXPLOSIVES"
    LAB_INSTRUMENTS="LAB_INSTRUMENTS"
    AMMUNITION="AMMUNITION"
    ELECTRONICS="ELECTRONICS"
    SHIP_PLATING="SHIP_PLATING"
    EQUIPMENT="EQUIPMENT"
    FUEL="FUEL"
    MEDICINE="MEDICINE"
    DRUGS="DRUGS"
    CLOTHING="CLOTHING"
    MICROPROCESSORS="MICROPROCESSORS"
    PLASTICS="PLASTICS"
    POLYNUCLEOTIDES="POLYNUCLEOTIDES"
    BIOCOMPOSITES="BIOCOMPOSITES"
    NANOBOTS="NANOBOTS"
    AI_MAINFRAMES="AI_MAINFRAMES"
    QUANTUM_DRIVES="QUANTUM_DRIVES"
    ROBOTIC_DRONES="ROBOTIC_DRONES"
    CYBER_IMPLANTS="CYBER_IMPLANTS"
    GENE_THERAPEUTICS="GENE_THERAPEUTICS"
    NEURAL_CHIPS="NEURAL_CHIPS"
    MOOD_REGULATORS="MOOD_REGULATORS"
    VIRAL_AGENTS="VIRAL_AGENTS"
    MICRO_FUSION_GENERATORS="MICRO_FUSION_GENERATORS"
    SUPERGRAINS="SUPERGRAINS"
    LASER_RIFLES="LASER_RIFLES"
    HOLOGRAPHICS="HOLOGRAPHICS"
    SHIP_SALVAGE="SHIP_SALVAGE"
    RELIC_TECH="RELIC_TECH"
    NOVEL_LIFEFORMS="NOVEL_LIFEFORMS"
    BOTANICAL_SPECIMENS="BOTANICAL_SPECIMENS"
    CULTURAL_ARTIFACTS="CULTURAL_ARTIFACTS"
    REACTOR_SOLAR_I="REACTOR_SOLAR_I"
    REACTOR_FUSION_I="REACTOR_FUSION_I"
    REACTOR_FISSION_I="REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I="REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I="REACTOR_ANTIMATTER_I"
    ENGINE_IMPULSE_DRIVE_I="ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I="ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II="ENGINE_ION_DRIVE_II"
    ENGINE_HYPER_DRIVE_I="ENGINE_HYPER_DRIVE_I"
    MODULE_MINERAL_PROCESSOR_I="MODULE_MINERAL_PROCESSOR_I"
    MODULE_CARGO_HOLD_I="MODULE_CARGO_HOLD_I"
    MODULE_CREW_QUARTERS_I="MODULE_CREW_QUARTERS_I"
    MODULE_ENVOY_QUARTERS_I="MODULE_ENVOY_QUARTERS_I"
    MODULE_PASSENGER_CABIN_I="MODULE_PASSENGER_CABIN_I"
    MODULE_MICRO_REFINERY_I="MODULE_MICRO_REFINERY_I"
    MODULE_ORE_REFINERY_I="MODULE_ORE_REFINERY_I"
    MODULE_FUEL_REFINERY_I="MODULE_FUEL_REFINERY_I"
    MODULE_SCIENCE_LAB_I="MODULE_SCIENCE_LAB_I"
    MODULE_JUMP_DRIVE_I="MODULE_JUMP_DRIVE_I"
    MODULE_JUMP_DRIVE_II="MODULE_JUMP_DRIVE_II"
    MODULE_JUMP_DRIVE_III="MODULE_JUMP_DRIVE_III"
    MODULE_SHIELD_GENERATOR_I="MODULE_SHIELD_GENERATOR_I"
    MODULE_SHIELD_GENERATOR_II="MODULE_SHIELD_GENERATOR_II"
    MOUNT_GAS_SIPHON_I="MOUNT_GAS_SIPHON_I"
    MOUNT_GAS_SIPHON_II="MOUNT_GAS_SIPHON_II"
    MOUNT_GAS_SIPHON_III="MOUNT_GAS_SIPHON_III"
    MOUNT_SURVEYOR_I="MOUNT_SURVEYOR_I"
    MOUNT_SURVEYOR_II="MOUNT_SURVEYOR_II"
    MOUNT_SURVEYOR_III="MOUNT_SURVEYOR_III"
    MOUNT_SENSOR_ARRAY_I="MOUNT_SENSOR_ARRAY_I"
    MOUNT_SENSOR_ARRAY_II="MOUNT_SENSOR_ARRAY_II"
    MOUNT_SENSOR_ARRAY_III="MOUNT_SENSOR_ARRAY_III"
    MOUNT_MINING_LASER_I="MOUNT_MINING_LASER_I"
    MOUNT_MINING_LASER_II="MOUNT_MINING_LASER_II"
    MOUNT_MINING_LASER_III="MOUNT_MINING_LASER_III"
    MOUNT_LASER_CANNON_I="MOUNT_LASER_CANNON_I"
    MOUNT_MISSILE_LAUNCHER_I="MOUNT_MISSILE_LAUNCHER_I"
    MOUNT_TURRET_I="MOUNT_TURRET_I"
class MarketTransactionType(myEnum):
    PURCHASE="PURCHASE"
    SELL="SELL"
class MarketTradeGoodSupply(myEnum):
    SCARCE="SCARCE"
    LIMITED="LIMITED"
    MODERATE="MODERATE"
    ABUNDANT="ABUNDANT"
class ShipModuleType(myEnum):
    MODULE_MINERAL_PROCESSOR_I="MODULE_MINERAL_PROCESSOR_I"
    MODULE_CARGO_HOLD_I="MODULE_CARGO_HOLD_I"
    MODULE_CREW_QUARTERS_I="MODULE_CREW_QUARTERS_I"
    MODULE_ENVOY_QUARTERS_I="MODULE_ENVOY_QUARTERS_I"
    MODULE_PASSENGER_CABIN_I="MODULE_PASSENGER_CABIN_I"
    MODULE_MICRO_REFINERY_I="MODULE_MICRO_REFINERY_I"
    MODULE_ORE_REFINERY_I="MODULE_ORE_REFINERY_I"
    MODULE_FUEL_REFINERY_I="MODULE_FUEL_REFINERY_I"
    MODULE_SCIENCE_LAB_I="MODULE_SCIENCE_LAB_I"
    MODULE_JUMP_DRIVE_I="MODULE_JUMP_DRIVE_I"
    MODULE_JUMP_DRIVE_II="MODULE_JUMP_DRIVE_II"
    MODULE_JUMP_DRIVE_III="MODULE_JUMP_DRIVE_III"
    MODULE_WARP_DRIVE_I="MODULE_WARP_DRIVE_I"
    MODULE_WARP_DRIVE_II="MODULE_WARP_DRIVE_II"
    MODULE_WARP_DRIVE_III="MODULE_WARP_DRIVE_III"
    MODULE_SHIELD_GENERATOR_I="MODULE_SHIELD_GENERATOR_I"
    MODULE_SHIELD_GENERATOR_II="MODULE_SHIELD_GENERATOR_II"
class ShipFrameType(myEnum):
    FRAME_PROBE="FRAME_PROBE"
    FRAME_DRONE="FRAME_DRONE"
    FRAME_INTERCEPTOR="FRAME_INTERCEPTOR"
    FRAME_RACER="FRAME_RACER"
    FRAME_FIGHTER="FRAME_FIGHTER"
    FRAME_FRIGATE="FRAME_FRIGATE"
    FRAME_SHUTTLE="FRAME_SHUTTLE"
    FRAME_EXPLORER="FRAME_EXPLORER"
    FRAME_LIGHT_FREIGHTER="FRAME_LIGHT_FREIGHTER"
    FRAME_HEAVY_FREIGHTER="FRAME_HEAVY_FREIGHTER"
    FRAME_TRANSPORT="FRAME_TRANSPORT"
    FRAME_DESTROYER="FRAME_DESTROYER"
    FRAME_CRUISER="FRAME_CRUISER"
    FRAME_CARRIER="FRAME_CARRIER"
    FRAME_MINER="FRAME_MINER"
class ShipMountType(myEnum):
    MOUNT_GAS_SIPHON_I="MOUNT_GAS_SIPHON_I"
    MOUNT_GAS_SIPHON_II="MOUNT_GAS_SIPHON_II"
    MOUNT_GAS_SIPHON_III="MOUNT_GAS_SIPHON_III"
    MOUNT_SURVEYOR_I="MOUNT_SURVEYOR_I"
    MOUNT_SURVEYOR_II="MOUNT_SURVEYOR_II"
    MOUNT_SURVEYOR_III="MOUNT_SURVEYOR_III"
    MOUNT_SENSOR_ARRAY_I="MOUNT_SENSOR_ARRAY_I"
    MOUNT_SENSOR_ARRAY_II="MOUNT_SENSOR_ARRAY_II"
    MOUNT_SENSOR_ARRAY_III="MOUNT_SENSOR_ARRAY_III"
    MOUNT_MINING_LASER_I="MOUNT_MINING_LASER_I"
    MOUNT_MINING_LASER_II="MOUNT_MINING_LASER_II"
    MOUNT_MINING_LASER_III="MOUNT_MINING_LASER_III"
    MOUNT_LASER_CANNON_I="MOUNT_LASER_CANNON_I"
    MOUNT_MISSILE_LAUNCHER_I="MOUNT_MISSILE_LAUNCHER_I"
    MOUNT_TURRET_I="MOUNT_TURRET_I"
class ShipCrewRotation(myEnum):
    STRICT="STRICT"
    RELAXED="RELAXED"
class ShipEngineType(myEnum):
    ENGINE_IMPULSE_DRIVE_I="ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I="ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II="ENGINE_ION_DRIVE_II"
    ENGINE_HYPER_DRIVE_I="ENGINE_HYPER_DRIVE_I"
class ShipReactorType(myEnum):
    REACTOR_SOLAR_I="REACTOR_SOLAR_I"
    REACTOR_FUSION_I="REACTOR_FUSION_I"
    REACTOR_FISSION_I="REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I="REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I="REACTOR_ANTIMATTER_I"
class SurveySize(myEnum):
    SMALL="SMALL"
    MODERATE="MODERATE"
    LARGE="LARGE"

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
    symbol: ShipEngineType
    requirements: ShipRequirements
    name:str
    description:str
    speed: int
    condition: Optional[int]
    def __init__(self,data) -> None:
        self.symbol=ShipEngineType[data["symbol"]]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"]
        self.speed=data["speed"].as_int_oapg
        self.condition=data["condition"].as_int_oapg if "condition" in data else None
@dataclass
class ShipReactor:
    symbol:ShipReactorType
    requirements: ShipRequirements
    name:str
    description:str
    powerOutput:int
    condition:Optional[int]
    def __init__(self,data) -> None:
        self.symbol=ShipReactorType[data["symbol"]]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"]
        self.powerOutput=data["powerOutput"].as_int_oapg
        self.condition=data["condition"].as_int_oapg if "condition" in data else None
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
    symbol:ShipModuleType
    requirements:ShipRequirements
    name:str
    capacity:Optional[int]
    range:Optional[int]
    description:Optional[str]
    def __init__(self,data) -> None:
        self.symbol=ShipModuleType[data["symbol"]]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.capacity=data["capacity"].as_int_oapg if "capacity" in data else None
        self.range=data["range"].as_int_oapg if "range" in data else None
        self.description=data["description"] if "description" in data else None
@dataclass
class ShipMount:
    symbol:ShipMountType
    requirements:ShipRequirements
    name:str
    description:Optional[str]
    strength:Optional[int]
    def __init__(self,data) -> None:
        self.symbol=ShipMountType[data["symbol"]]
        self.requirements=ShipRequirements(data["requirements"])
        self.name=data["name"]
        self.description=data["description"] if "description" in data else None
        self.strength=data["strength"].as_int_oapg if "strength" in data else None
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
    symbol:ShipFrameType
    moduleSlots:int
    requirements:ShipRequirements
    fuelCapacity:int
    name:str
    description:str
    mountingPoints:int
    condition:Optional[int]
    def __init__(self,data) -> None:
        self.symbol=ShipFrameType[data["symbol"]]
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
    rotation:ShipCrewRotation
    morale:int
    required:int
    capacity:int
    def __init__(self,data) -> None:
        self.wages=data["wages"].as_int_oapg
        self.current=data["current"].as_int_oapg
        self.rotation=ShipCrewRotation[data["rotation"]]
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
    type:WaypointType
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.systemSymbol=data["systemSymbol"]
        self.x=data["x"].as_int_oapg
        self.y=data["y"].as_int_oapg
        self.type=WaypointType[data["type"]]
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
    symbol:str
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
        self.symbol = data["symbol"]
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
class TradeGood:
    symbol:TradeSymbol
    name:str
    description:str
    def __init__(self,data) -> None:
        self.symbol=TradeSymbol[data["symbol"]]
        self.name=data["name"]
        self.description=data["description"]
@dataclass
class MarketTransaction:
    shipSymbol:str
    units:int
    type:MarketTransactionType
    pricePerUnit:int
    timestamp:str
    tradeSymbol:str
    totalPrice:int
    def __init__(self,data) -> None:
        self.shipSymbol=data["shipSymbol"]
        self.units=data["units"].as_int_oapg
        self.type=MarketTransactionType[data["type"]]
        self.pricePerUnit=data["pricePerUnit"].as_int_oapg
        self.timestamp=data["timestamp"]
        self.tradeSymbol=data["tradeSymbol"]
        self.totalPrice=data["totalPrice"].as_int_oapg
@dataclass
class MarketTradeGood:
    tradeVolume:int
    symbol:str
    sellPrice:int
    purchasePrice:int
    supply:MarketTradeGoodSupply
    def __init__(self,data) -> None:
        self.tradeVolume=data["tradeVolume"].as_int_oapg
        self.symbol=data["symbol"]
        self.sellPrice=data["sellPrice"].as_int_oapg
        self.purchasePrice=data["purchasePrice"].as_int_oapg
        self.supply=MarketTradeGoodSupply[data["supply"]]
@dataclass
class Market:
    symbol:str
    imports:list[TradeGood]
    exports:list[TradeGood]
    exchange:list[TradeGood]
    transactions:Optional[list[MarketTransaction]]
    tradeGoods:Optional[list[MarketTradeGood]]
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.imports=[TradeGood(t) for t in data["imports"]]
        self.exports=[TradeGood(t) for t in data["exports"]]
        self.exchange=[TradeGood(t) for t in data["exchange"]]
        self.transactions=[MarketTransaction(t) for t in data["transactions"]] if "transactions" in data else None
        self.tradeGoods=[MarketTradeGood(t) for t in data["tradeGoods"]] if "tradeGoods" in data else None
@dataclass
class ConnectedSystem:
    symbol:str
    distance:int
    sectorSymbol:str
    x:int
    y:int
    type:SystemType
    factionSymbol:Optional[str]
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.distance=data["distance"].as_int_oapg
        self.sectorSymbol=data["sectorSymbol"]
        self.x=data["x"].as_int_oapg
        self.y=data["y"].as_int_oapg
        self.type=SystemType[data["type"]]
        self.factionSymbol=data["factionSymbol"] if "factionSymbol" in data else None
@dataclass
class JumpGate:
    connectedSystems:list[ConnectedSystem]
    jumpRange:int
    factionSymbol:Optional[str]
    def __init__(self,data) -> None:
        self.connectedSystems=[ConnectedSystem(s) for s in data["connectedSystems"]]
        self.jumpRange=data["jumpRange"].as_int_oapg
        self.factionSymbol=data["factionSymbol"] if "factionSymbol" in data else None
@dataclass
class Cooldown:
    remainingSeconds:int
    totalSeconds:int
    expiration:str
    shipSymbol:str
    def __init__(self,data) -> None:
        self.remainingSeconds=data["remainingSeconds"].as_int_oapg
        self.totalSeconds=data["totalSeconds"].as_int_oapg
        self.expiration=data["expiration"]
        self.shipSymbol=data["shipSymbol"]
@dataclass
class SurveyDeposit:
    symbol:str
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
@dataclass
class Survey:
    symbol:str
    size:SurveySize
    signature:str
    expiration:str
    deposits:list[SurveyDeposit]
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.size=SurveySize[data["size"]]
        self.signature=data["signature"]
        self.expiration=data["expiration"]
        self.deposits=[SurveyDeposit(d) for d in data["deposits"]]
    def dict(self):
        return {"signature":self.signature,"symbol":self.symbol,"deposits":[{"symbol":x.symbol} for x in self.deposits],"expiration":self.expiration,"size":self.size.name}
@dataclass
class ExtractionYield:
    symbol:str
    units:int
    def __init__(self,data) -> None:
        self.symbol=data["symbol"]
        self.units=data["units"].as_int_oapg
@dataclass
class Extraction:
    yield_:ExtractionYield
    shipSymbol:str
    def __init__(self,data) -> None:
        self.yield_=ExtractionYield(data["yield"])
        self.shipSymbol=data["shipSymbol"]
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
    agent: Agent
    ships: dict[str,Ship]

    def __init__(self,token=None) -> None:
        configuration = openapi_client.Configuration()
        if token == None:
            try:
                with open(PATH_PREFIX+"acc.txt", "r") as f:
                    configuration.access_token = f.readline().replace("\n", "")
            except:
                pass
        else:
            configuration.access_token = token
        self.api_client = openapi_client.ApiClient(configuration)

        self.api_agents = agents_api.AgentsApi(self.api_client)
        self.api_contracts = contracts_api.ContractsApi(self.api_client)
        self.def_api = default_api.DefaultApi(self.api_client)
        self.api_factions = factions_api.FactionsApi(self.api_client)
        self.api_fleet = fleet_api.FleetApi(self.api_client)
        self.api_systems = systems_api.SystemsApi(self.api_client)

        self.ships={}

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
    def accept_contract(self, contractId):
        try:
            api_response = self.api_contracts.accept_contract(path_params={"contractId": contractId})
            return (Agent(api_response.body["data"]["agent"]),Contract(api_response.body["data"]["contract"]))
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->accept_contract: %s\n" % e)
    def deliver_contract(self, contractId, tradeSymbol, shipSymbol, units):
        try:
            api_response = self.api_contracts.deliver_contract(path_params={"contractId": contractId}, body={"tradeSymbol": tradeSymbol, "shipSymbol": shipSymbol, "units": units})

            return (Contract(api_response.body["data"]["contract"]),ShipCargo(api_response.body["data"]["cargo"]))
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
    def create_chart(self, shipSymbol):
        try:
            api_response = self.api_fleet.create_chart(path_params={"shipSymbol": shipSymbol})
            waypoint = Waypoint(api_response.body["data"]["waypoint"])
            chart = Chart(api_response.body["data"]["chart"])
            return (waypoint,chart)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->create_chart: %s\n" % e)
    
    def create_survey(self,shipSymbol):
        try:
            api_response = self.api_fleet.create_survey(path_params={"shipSymbol": shipSymbol})
            return (Cooldown(api_response.body["data"]["cooldown"]),[Survey(s) for s in api_response.body["data"]["surveys"]])
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->create_survey: %s\n" % e)
    def dock_ship(self,shipSymbol):
        try:
            api_response = self.api_fleet.dock_ship(path_params={"shipSymbol": shipSymbol})
            nav = ShipNav(api_response.body["data"]["nav"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav=nav
            return nav
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->dock_ship: %s\n" % e)
    def extract_resources(self,shipSymbol,survey=None):
        try:
            api_response = self.api_fleet.extract_resources(path_params={"shipSymbol": shipSymbol},body={"survey":survey.dict()} if survey!=None else {})
            return (Cooldown(api_response.body["data"]["cooldown"]),ShipCargo(api_response.body["data"]["cargo"]),Extraction(api_response.body["data"]["extraction"]))
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->extract_resources: %s\n" % e)
    def get_my_ship(self,shipSymbol):
        try:
            api_response = self.api_fleet.get_my_ship(path_params={"shipSymbol": shipSymbol})
            ship = Ship(api_response.body["data"])
            self.ships[ship.symbol]=ship
            return ship
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->get_my_ship: %s\n" % e)
    def get_my_ships(self):
        try:
            api_response = self.api_fleet.get_my_ships()
            pprint(api_response.body["meta"])
            ships = [Ship(k) for k in api_response.body["data"]]
            for s in ships:
                self.ships[s.symbol]=s
            return ships 
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->get_my_ships: %s\n" % e)

    def jettison(self,shipSymbol,good,units):
        try:
            api_response = self.api_fleet.jettison(path_params={"shipSymbol": shipSymbol},body={"symbol":good,"units":units})
            cargo = ShipCargo(api_response.body["data"]["cargo"]) 
            if shipSymbol in self.ships:
                self.ships[shipSymbol].cargo=cargo
            return cargo
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->jettison: %s\n" % e)

    def navigate_ship(self,shipSymbol,waypointSymbol):
        try:
            api_response = self.api_fleet.navigate_ship(path_params={"shipSymbol": shipSymbol},body={"waypointSymbol":waypointSymbol})
            nav = ShipNav(api_response.body["data"]["nav"])
            fuel = ShipFuel(api_response.body["data"]["fuel"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav = nav
                self.ships[shipSymbol].fuel = fuel
            return (nav,fuel)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->navigate_ship: %s\n" % e)
    def orbit_ship(self,shipSymbol):
        try:
            api_response = self.api_fleet.orbit_ship(path_params={"shipSymbol": shipSymbol})
            nav = ShipNav(api_response.body["data"]["nav"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav=nav
            return nav
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->orbit_ship: %s\n" % e)
    
    def purchase_ship(self, waypointSymbol,shipType):
        try:
            api_response = self.api_fleet.purchase_ship(body={"waypointSymbol": waypointSymbol,"shipType":shipType})
            return (Agent(api_response.body["data"]["agent"]),Ship(api_response.body["data"]["ship"]))
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->purchase_ship: %s\n" % e)
    def refuel_ship(self,shipSymbol):
        try:
            api_response = self.api_fleet.refuel_ship(path_params={"shipSymbol": shipSymbol})
            return (Agent(api_response.body["data"]["agent"]),ShipFuel(api_response.body["data"]["fuel"]))
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->refuel_ship: %s\n" % e)
    def sell_cargo(self,shipSymbol,good,units):
        try:
            api_response = self.api_fleet.sell_cargo(path_params={"shipSymbol": shipSymbol},body={"symbol":good,"units":units})
            self.agent = Agent(api_response.body["data"]["agent"])
            cargo = ShipCargo(api_response.body["data"]["cargo"])
            transaction = MarketTransaction(api_response.body["data"]["transaction"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].cargo=cargo
            return (self.agent,cargo,transaction)

        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->sell_cargo: %s\n" % e)
    def transfer_cargo(self,shipSymbol,good,units,receivingShipSymbol):
        try:
            api_response = self.api_fleet.transfer_cargo(path_params={"shipSymbol": shipSymbol},body={"tradeSymbol":good,"units":units,"shipSymbol":receivingShipSymbol})
            return (ShipCargo(api_response.body["data"]["cargo"]))
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->transfer_cargo: %s\n" % e)
    
    
    # endregion
    
    # region SystemsApi
    def get_waypoint(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_waypoint(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            return Waypoint(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_waypoint: %s\n" % e)
    def get_jump_gate(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_jump_gate(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            return JumpGate(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_jump_gate: %s\n" % e)
    def get_market(self,waypointSymbol):
        try:
            api_response = self.api_systems.get_market(path_params={"systemSymbol": waypointSymbol[0:waypointSymbol.find("-",4)],"waypointSymbol":waypointSymbol})
            return Market(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_market: %s\n" % e)
    def get_shipyard(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_shipyard(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
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

    #region asdf
    def timestamp_to_duration(self,timestamp):
        return (datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S.%fZ") - datetime.utcnow()).total_seconds()
    #endregion

    #region nop
    def nop(): pass # VS Code wont let me close the last region that contains a def so this is a fix for that
    #endregion

if __name__ == "__main__":
    st = SpaceTraders()
    prices = {"SHIP_PROBE":69972,"SHIP_MINING_DRONE":87220,"SHIP_ORE_HOUND":159220,"SHIP_REFINING_FREIGHTER":1696320}
    # st.register("test0003","COSMIC")
    # pprint(st.get_factions())
    # exit()
    # pprint(st.get_agent())
    system = "X1-UV97"
    waypoint = "X1-UV97-21170Z"
    shipyardWaypoint = "X1-UV97-44217E"
    jumpWaypoint = "X1-UV97-23539X"
    ship = "FEBATE5T-1"
    drone = "FEBATE5T-2"
    asteroidField ="X1-UV97-24895D"
    contractId="clc3oyf4l000ss60j6lzyx2mv"
    contractIce ="X1-UV97-21170Z"
    copperAlu="X1-UV97-57201E"
    silverGoldPlat="X1-UV97-82653Z"
    # pprint(st.get_waypoint(system,waypoint))
    # pprint(st.get_system(system))
    # pprint(st.get_systems())
    # pprint(st.get_system_waypoints(system))
    # pprint(st.get_shipyard(system,shipyardWaypoint))
    # pprint(st.get_market(system,shipyardWaypoint))
    # pprint(st.get_jump_gate(system,jumpWaypoint))
    # pprint(st.get_contract("clc3oyf4l000ss60j6lzyx2mv"))
    # pprint(st.get_contracts())

    # pprint(st.get_my_ships())
    # pprint(st.create_chart(ship))
    # pprint(st.get_my_ship(ship))

    # pprint(st.orbit_ship(ship))
    # pprint(st.navigate_ship(ship,asteroidField))

    # cooldown,surveys=st.create_survey(ship)
    # pprint((cooldown,surveys))
    # pprint(st.dock_ship(ship))
    # time.sleep(cooldown.remainingSeconds)
    # pprint(st.extract_resources(ship,surveys[0]))
    # while True:
    #     r = st.extract_resources(ship)
    #     pprint(r)
    #     time.sleep(r[0].totalSeconds)

    # pprint(st.navigate_ship(ship,"X1-UV97-25702Z"))
    # pprint(st.get_my_ships())
    # pprint(st.sell_cargo(ship,"AMMONIA_ICE",16))
    # pprint(st.get_market(system,"X1-UV97-25702Z"))
    # waypoints = st.get_system_waypoints(system)
    # pprint(waypoints)
    # markets,shipyards=[],[]
    # for w in waypoints:
    #     print(w.symbol)
    #     if WaypointTraitSymbols.MARKETPLACE in [x.symbol for x in w.traits]:
    #         markets.append(w)
    #         m = st.get_market(system,w.symbol)
    #         pprint(([x.symbol for x in m.imports],[x.symbol for x in m.exports],[x.symbol for x in m.exchange]))
    #     if WaypointTraitSymbols.SHIPYARD in [x.symbol for x in w.traits]:
    #         shipyards.append(w)
    #         pprint(st.get_shipyard(system,w.symbol))
    # pprint(st.navigate_ship(ship,"X1-UV97-44217E"))
    # pprint(st.purchase_ship(shipyardWaypoint,"SHIP_PROBE"))

    # pprint(st.accept_contract(contractId))
    # st.orbit_ship(ship)
    # pprint(st.navigate_ship(ship,asteroidField))
    def handleCargo(shipsymbol):
        cargo = st.ships[shipsymbol].cargo
        icewaterway   = "X1-UV97-21170Z"
        ammoniaiceway = "X1-UV97-25702Z"
        contractId="clc3oyf4l000ss60j6lzyx2mv"
        inplace = [TradeSymbol.COPPER_ORE,TradeSymbol.ALUMINUM_ORE,TradeSymbol.SILVER_ORE,TradeSymbol.GOLD_ORE,TradeSymbol.PLATINUM_ORE]
        pprint([x.symbol for x in cargo.inventory])
        for good in inplace:
            print(good)
            if str(good) in [x.symbol for x in cargo.inventory]:
                st.dock_ship(shipsymbol)
                pprint(st.sell_cargo(shipsymbol,str(good),sum([x.units if x.symbol == str(good) else 0 for x in cargo.inventory]))[2])
        
        if "ICE_WATER" in [x.symbol for x in cargo.inventory] or "IRON_ORE" in [x.symbol for x in cargo.inventory]:
            st.orbit_ship(shipsymbol)
            r = st.navigate_ship(shipsymbol,icewaterway)
            pprint(r)
            t = st.timestamp_to_duration(r[0].route.arrival)
            time.sleep(t)
            st.dock_ship(shipsymbol)
            if "ICE_WATER" in [x.symbol for x in cargo.inventory]:
                pprint(st.sell_cargo(shipsymbol,"ICE_WATER",sum([x.units if x.symbol == "ICE_WATER" else 0 for x in cargo.inventory])))
            if "IRON_ORE" in [x.symbol for x in cargo.inventory]:
                pprint(st.deliver_contract(contractId,"IRON_ORE",shipsymbol,sum([x.units if x.symbol == "IRON_ORE" else 0 for x in cargo.inventory])))
        
        if "AMMONIA_ICE" in [x.symbol for x in cargo.inventory]:
            st.orbit_ship(shipsymbol)
            r = st.navigate_ship(shipsymbol,ammoniaiceway)
            pprint(r)
            t = st.timestamp_to_duration(r[0].route.arrival)
            time.sleep(t)
            st.dock_ship(shipsymbol)
            pprint(st.sell_cargo(shipsymbol,"AMMONIA_ICE",sum([x.units if x.symbol == "AMMONIA_ICE" else 0 for x in cargo.inventory])))
    def dumpunused(shipsymbol):
        cargo = st.ships[shipsymbol].cargo
        if "QUARTZ_SAND" in [x.symbol for x in cargo.inventory]:
            pprint(st.jettison(shipsymbol,"QUARTZ_SAND",sum([x.units if x.symbol == "QUARTZ_SAND" else 0 for x in cargo.inventory])))

        if "SILICON_CRYSTALS" in [x.symbol for x in cargo.inventory]:
            pprint(st.jettison(shipsymbol,"SILICON_CRYSTALS",sum([x.units if x.symbol == "SILICON_CRYSTALS" else 0 for x in cargo.inventory])))
        
    # pprint(st.get_my_ship(drone).cargo)
    # pprint(st.get_my_ship(ship).cargo)
    # handleCargo(ship,st.get_my_ship(ship).cargo)
    pprint(st.get_my_ships())
    # handleCargo(ship)

    # r = st.navigate_ship(ship,asteroidField)
    # pprint(r)
    
    # t = st.timestamp_to_duration(r[0].route.arrival)
    # time.sleep(t)

    # pprint(st.navigate_ship(ship,asteroidField))
    # pprint(st.jettison(ship,"QUARTZ_SAND",13))
    # pprint(st.get_market("X1-UV97-21170Z"))
    # pprint(st.navigate_ship(ship,"X1-UV97-25702Z"))
    # pprint(st.get_market("X1-UV97-25702Z"))
    # st.dock_ship(ship)
    # pprint(st.refuel_ship(ship))
    # pprint(st.)
    # pprint(st.transfer_cargo(ship,"ANTIMATTER",15,drone))
    # pprint(st.transfer_cargo(drone,"ICE_WATER",15,ship))

    def dumbsell(shipsymbol):
        cargo = st.ships[shipsymbol].cargo

        inplace = [TradeSymbol.IRON_ORE,TradeSymbol.COPPER_ORE,TradeSymbol.ALUMINUM_ORE,TradeSymbol.SILVER_ORE,TradeSymbol.GOLD_ORE,TradeSymbol.PLATINUM_ORE]
        for good in inplace:
            if str(good) in [x.symbol for x in cargo.inventory]:
                pprint(st.sell_cargo(shipsymbol,str(good),sum([x.units if x.symbol == str(good) else 0 for x in cargo.inventory]))[2])
        
        dump = "ICE_WATER","AMMONIA_ICE","QUARTZ_SAND","SILICON_CRYSTALS"
        for good in dump:
            if good in [x.symbol for x in cargo.inventory]:
                pprint(st.jettison(shipsymbol,good,sum([x.units if x.symbol == good else 0 for x in cargo.inventory])))
        
    
    st.dock_ship(ship)
    st.dock_ship(drone)
    # while True:
    #     dumbsell(ship)
    #     dumbsell(drone)
    #     pprint(st.extract_resources(ship)[2])
    #     pprint(st.extract_resources(drone)[2])
    # #     dumpunused(ship)
    # #     dumpunused(drone)
    #     pprint(st.agent.credits)
    #     time.sleep(60)
    # pprint(st.get_market(copperAlu))

    pprint([x.symbol for x in st.get_factions()])


    # st.dock_ship(ship)
    # pprint(st.refuel_ship(ship))
    # pprint(st.get_agent())
    # pprint(st.get_my_ship(drone))
    # pprint(st.transfer_cargo(ship,"ICE_WATER",11,drone))
    # pprint(st.transfer_cargo(ship,"QUARTZ_SAND",10,drone))
    # st.dock_ship(ship)
    # pprint(st.sell_cargo(ship,"COPPER_ORE",8))
    # pprint(st.get_shipyard(system,"X1-UV97-44217E"))