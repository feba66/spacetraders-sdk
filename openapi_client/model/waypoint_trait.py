# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is a multiplayer sci-fi strategy game where you acquire and manage a fleet of ships across a growing and dynamic universe.  Similar to games such as Eve Online, you work with or against other players to establish trade routes, chart new systems, mine precious ores, patrol for pirates, spy on factions, and discover hidden treasures.  SpaceTraders as a game is unique in that it is entirely accessible through open and well-documented API endpoints.  If this sounds fun and interesting to you, please drop into our Discord and get to know the community. We are actively working on new clients, new ideas and sharing tips for how to play the game.   ```json http {   \"method\": \"GET\",   \"url\": \"https://api-server-2-0-0-rc-2-vxxwq5xqdq-uc.a.run.app\", } ```  # noqa: E501

    The version of the OpenAPI document: 2.0.0-rc.2
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class WaypointTrait(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "name",
            "description",
        }
        
        class properties:
            
            
            class symbol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UNCHARTED": "UNCHARTED",
                        "MARKETPLACE": "MARKETPLACE",
                        "SHIPYARD": "SHIPYARD",
                        "OUTPOST": "OUTPOST",
                        "SCATTERED_SETTLEMENTS": "SCATTERED_SETTLEMENTS",
                        "SPRAWLING_CITIES": "SPRAWLING_CITIES",
                        "MEGA_STRUCTURES": "MEGA_STRUCTURES",
                        "OVERCROWDED": "OVERCROWDED",
                        "HIGH_TECH": "HIGH_TECH",
                        "CORRUPT": "CORRUPT",
                        "BUREAUCRATIC": "BUREAUCRATIC",
                        "TRADING_HUB": "TRADING_HUB",
                        "INDUSTRIAL": "INDUSTRIAL",
                        "BLACK_MARKET": "BLACK_MARKET",
                        "RESEARCH_FACILITY": "RESEARCH_FACILITY",
                        "MILITARY_BASE": "MILITARY_BASE",
                        "SURVEILLANCE_OUTPOST": "SURVEILLANCE_OUTPOST",
                        "EXPLORATION_OUTPOST": "EXPLORATION_OUTPOST",
                        "MINERAL_DEPOSITS": "MINERAL_DEPOSITS",
                        "COMMON_METAL_DEPOSITS": "COMMON_METAL_DEPOSITS",
                        "PRECIOUS_METAL_DEPOSITS": "PRECIOUS_METAL_DEPOSITS",
                        "RARE_METAL_DEPOSITS": "RARE_METAL_DEPOSITS",
                        "METHANE_POOLS": "METHANE_POOLS",
                        "ICE_CRYSTALS": "ICE_CRYSTALS",
                        "EXPLOSIVE_GASES": "EXPLOSIVE_GASES",
                        "STRONG_MAGNETOSPHERE": "STRONG_MAGNETOSPHERE",
                        "VIBRANT_AURORAS": "VIBRANT_AURORAS",
                        "SALT_FLATS": "SALT_FLATS",
                        "CANYONS": "CANYONS",
                        "PERPETUAL_DAYLIGHT": "PERPETUAL_DAYLIGHT",
                        "PERPETUAL_OVERCAST": "PERPETUAL_OVERCAST",
                        "DRY_SEABEDS": "DRY_SEABEDS",
                        "MAGMA_SEAS": "MAGMA_SEAS",
                        "SUPERVOLCANOES": "SUPERVOLCANOES",
                        "ASH_CLOUDS": "ASH_CLOUDS",
                        "VAST_RUINS": "VAST_RUINS",
                        "MUTATED_FLORA": "MUTATED_FLORA",
                        "TERRAFORMED": "TERRAFORMED",
                        "EXTREME_TEMPERATURES": "EXTREME_TEMPERATURES",
                        "EXTREME_PRESSURE": "EXTREME_PRESSURE",
                        "DIVERSE_LIFE": "DIVERSE_LIFE",
                        "SCARCE_LIFE": "SCARCE_LIFE",
                        "FOSSILS": "FOSSILS",
                        "WEAK_GRAVITY": "WEAK_GRAVITY",
                        "STRONG_GRAVITY": "STRONG_GRAVITY",
                        "CRUSHING_GRAVITY": "CRUSHING_GRAVITY",
                        "TOXIC_ATMOSPHERE": "TOXIC_ATMOSPHERE",
                        "CORROSIVE_ATMOSPHERE": "CORROSIVE_ATMOSPHERE",
                        "BREATHABLE_ATMOSPHERE": "BREATHABLE_ATMOSPHERE",
                        "JOVIAN": "JOVIAN",
                        "ROCKY": "ROCKY",
                        "VOLCANIC": "VOLCANIC",
                        "FROZEN": "FROZEN",
                        "SWAMP": "SWAMP",
                        "BARREN": "BARREN",
                        "TEMPERATE": "TEMPERATE",
                        "JUNGLE": "JUNGLE",
                        "OCEAN": "OCEAN",
                        "STRIPPED": "STRIPPED",
                    }
                
                @schemas.classproperty
                def UNCHARTED(cls):
                    return cls("UNCHARTED")
                
                @schemas.classproperty
                def MARKETPLACE(cls):
                    return cls("MARKETPLACE")
                
                @schemas.classproperty
                def SHIPYARD(cls):
                    return cls("SHIPYARD")
                
                @schemas.classproperty
                def OUTPOST(cls):
                    return cls("OUTPOST")
                
                @schemas.classproperty
                def SCATTERED_SETTLEMENTS(cls):
                    return cls("SCATTERED_SETTLEMENTS")
                
                @schemas.classproperty
                def SPRAWLING_CITIES(cls):
                    return cls("SPRAWLING_CITIES")
                
                @schemas.classproperty
                def MEGA_STRUCTURES(cls):
                    return cls("MEGA_STRUCTURES")
                
                @schemas.classproperty
                def OVERCROWDED(cls):
                    return cls("OVERCROWDED")
                
                @schemas.classproperty
                def HIGH_TECH(cls):
                    return cls("HIGH_TECH")
                
                @schemas.classproperty
                def CORRUPT(cls):
                    return cls("CORRUPT")
                
                @schemas.classproperty
                def BUREAUCRATIC(cls):
                    return cls("BUREAUCRATIC")
                
                @schemas.classproperty
                def TRADING_HUB(cls):
                    return cls("TRADING_HUB")
                
                @schemas.classproperty
                def INDUSTRIAL(cls):
                    return cls("INDUSTRIAL")
                
                @schemas.classproperty
                def BLACK_MARKET(cls):
                    return cls("BLACK_MARKET")
                
                @schemas.classproperty
                def RESEARCH_FACILITY(cls):
                    return cls("RESEARCH_FACILITY")
                
                @schemas.classproperty
                def MILITARY_BASE(cls):
                    return cls("MILITARY_BASE")
                
                @schemas.classproperty
                def SURVEILLANCE_OUTPOST(cls):
                    return cls("SURVEILLANCE_OUTPOST")
                
                @schemas.classproperty
                def EXPLORATION_OUTPOST(cls):
                    return cls("EXPLORATION_OUTPOST")
                
                @schemas.classproperty
                def MINERAL_DEPOSITS(cls):
                    return cls("MINERAL_DEPOSITS")
                
                @schemas.classproperty
                def COMMON_METAL_DEPOSITS(cls):
                    return cls("COMMON_METAL_DEPOSITS")
                
                @schemas.classproperty
                def PRECIOUS_METAL_DEPOSITS(cls):
                    return cls("PRECIOUS_METAL_DEPOSITS")
                
                @schemas.classproperty
                def RARE_METAL_DEPOSITS(cls):
                    return cls("RARE_METAL_DEPOSITS")
                
                @schemas.classproperty
                def METHANE_POOLS(cls):
                    return cls("METHANE_POOLS")
                
                @schemas.classproperty
                def ICE_CRYSTALS(cls):
                    return cls("ICE_CRYSTALS")
                
                @schemas.classproperty
                def EXPLOSIVE_GASES(cls):
                    return cls("EXPLOSIVE_GASES")
                
                @schemas.classproperty
                def STRONG_MAGNETOSPHERE(cls):
                    return cls("STRONG_MAGNETOSPHERE")
                
                @schemas.classproperty
                def VIBRANT_AURORAS(cls):
                    return cls("VIBRANT_AURORAS")
                
                @schemas.classproperty
                def SALT_FLATS(cls):
                    return cls("SALT_FLATS")
                
                @schemas.classproperty
                def CANYONS(cls):
                    return cls("CANYONS")
                
                @schemas.classproperty
                def PERPETUAL_DAYLIGHT(cls):
                    return cls("PERPETUAL_DAYLIGHT")
                
                @schemas.classproperty
                def PERPETUAL_OVERCAST(cls):
                    return cls("PERPETUAL_OVERCAST")
                
                @schemas.classproperty
                def DRY_SEABEDS(cls):
                    return cls("DRY_SEABEDS")
                
                @schemas.classproperty
                def MAGMA_SEAS(cls):
                    return cls("MAGMA_SEAS")
                
                @schemas.classproperty
                def SUPERVOLCANOES(cls):
                    return cls("SUPERVOLCANOES")
                
                @schemas.classproperty
                def ASH_CLOUDS(cls):
                    return cls("ASH_CLOUDS")
                
                @schemas.classproperty
                def VAST_RUINS(cls):
                    return cls("VAST_RUINS")
                
                @schemas.classproperty
                def MUTATED_FLORA(cls):
                    return cls("MUTATED_FLORA")
                
                @schemas.classproperty
                def TERRAFORMED(cls):
                    return cls("TERRAFORMED")
                
                @schemas.classproperty
                def EXTREME_TEMPERATURES(cls):
                    return cls("EXTREME_TEMPERATURES")
                
                @schemas.classproperty
                def EXTREME_PRESSURE(cls):
                    return cls("EXTREME_PRESSURE")
                
                @schemas.classproperty
                def DIVERSE_LIFE(cls):
                    return cls("DIVERSE_LIFE")
                
                @schemas.classproperty
                def SCARCE_LIFE(cls):
                    return cls("SCARCE_LIFE")
                
                @schemas.classproperty
                def FOSSILS(cls):
                    return cls("FOSSILS")
                
                @schemas.classproperty
                def WEAK_GRAVITY(cls):
                    return cls("WEAK_GRAVITY")
                
                @schemas.classproperty
                def STRONG_GRAVITY(cls):
                    return cls("STRONG_GRAVITY")
                
                @schemas.classproperty
                def CRUSHING_GRAVITY(cls):
                    return cls("CRUSHING_GRAVITY")
                
                @schemas.classproperty
                def TOXIC_ATMOSPHERE(cls):
                    return cls("TOXIC_ATMOSPHERE")
                
                @schemas.classproperty
                def CORROSIVE_ATMOSPHERE(cls):
                    return cls("CORROSIVE_ATMOSPHERE")
                
                @schemas.classproperty
                def BREATHABLE_ATMOSPHERE(cls):
                    return cls("BREATHABLE_ATMOSPHERE")
                
                @schemas.classproperty
                def JOVIAN(cls):
                    return cls("JOVIAN")
                
                @schemas.classproperty
                def ROCKY(cls):
                    return cls("ROCKY")
                
                @schemas.classproperty
                def VOLCANIC(cls):
                    return cls("VOLCANIC")
                
                @schemas.classproperty
                def FROZEN(cls):
                    return cls("FROZEN")
                
                @schemas.classproperty
                def SWAMP(cls):
                    return cls("SWAMP")
                
                @schemas.classproperty
                def BARREN(cls):
                    return cls("BARREN")
                
                @schemas.classproperty
                def TEMPERATE(cls):
                    return cls("TEMPERATE")
                
                @schemas.classproperty
                def JUNGLE(cls):
                    return cls("JUNGLE")
                
                @schemas.classproperty
                def OCEAN(cls):
                    return cls("OCEAN")
                
                @schemas.classproperty
                def STRIPPED(cls):
                    return cls("STRIPPED")
            name = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "symbol": symbol,
                "name": name,
                "description": description,
            }
    
    symbol: MetaOapg.properties.symbol
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "name", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WaypointTrait':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            name=name,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
