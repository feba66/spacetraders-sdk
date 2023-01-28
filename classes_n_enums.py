from dataclasses import dataclass
from enum import Enum
from typing import Optional
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
    GOOD_NOT_AVAILABLE_AT_MARKET= 4602
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
    MODULE_WARP_DRIVE_I="MODULE_WARP_DRIVE_I"
    MODULE_WARP_DRIVE_II="MODULE_WARP_DRIVE_II"
    MODULE_WARP_DRIVE_III="MODULE_WARP_DRIVE_III"
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
