# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is a multiplayer sci-fi strategy game where you acquire and manage a fleet of ships across a growing and dynamic universe.  Similar to games such as Eve Online, you work with or against other players to establish trade routes, chart new systems, mine precious ores, patrol for pirates, spy on factions, and discover hidden treasures.  SpaceTraders as a game is unique in that it is entirely accessible through open and well-documented API endpoints.  If this sounds fun and interesting to you, please drop into our Discord and get to know the community. We are actively working on new clients, new ideas and sharing tips for how to play the game.   ```json http {   \"method\": \"GET\",   \"url\": \"https://v2.api.spacetraders.io\", } ```  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class Waypoint(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.
    """


    class MetaOapg:
        required = {
            "symbol",
            "traits",
            "systemSymbol",
            "x",
            "y",
            "type",
            "orbitals",
        }
        
        class properties:
            
            
            class symbol(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def type() -> typing.Type['WaypointType']:
                return WaypointType
            
            
            class systemSymbol(
                schemas.StrSchema
            ):
                pass
            x = schemas.IntSchema
            y = schemas.IntSchema
            
            
            class orbitals(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WaypointOrbital']:
                        return WaypointOrbital
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WaypointOrbital'], typing.List['WaypointOrbital']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'orbitals':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WaypointOrbital':
                    return super().__getitem__(i)
            
            
            class traits(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WaypointTrait']:
                        return WaypointTrait
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WaypointTrait'], typing.List['WaypointTrait']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'traits':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WaypointTrait':
                    return super().__getitem__(i)
        
            @staticmethod
            def faction() -> typing.Type['WaypointFaction']:
                return WaypointFaction
        
            @staticmethod
            def chart() -> typing.Type['Chart']:
                return Chart
            __annotations__ = {
                "symbol": symbol,
                "type": type,
                "systemSymbol": systemSymbol,
                "x": x,
                "y": y,
                "orbitals": orbitals,
                "traits": traits,
                "faction": faction,
                "chart": chart,
            }
    
    symbol: MetaOapg.properties.symbol
    traits: MetaOapg.properties.traits
    systemSymbol: MetaOapg.properties.systemSymbol
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    type: 'WaypointType'
    orbitals: MetaOapg.properties.orbitals
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'WaypointType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemSymbol"]) -> MetaOapg.properties.systemSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orbitals"]) -> MetaOapg.properties.orbitals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["traits"]) -> MetaOapg.properties.traits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["faction"]) -> 'WaypointFaction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chart"]) -> 'Chart': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "type", "systemSymbol", "x", "y", "orbitals", "traits", "faction", "chart", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'WaypointType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemSymbol"]) -> MetaOapg.properties.systemSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orbitals"]) -> MetaOapg.properties.orbitals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["traits"]) -> MetaOapg.properties.traits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["faction"]) -> typing.Union['WaypointFaction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chart"]) -> typing.Union['Chart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "type", "systemSymbol", "x", "y", "orbitals", "traits", "faction", "chart", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        traits: typing.Union[MetaOapg.properties.traits, list, tuple, ],
        systemSymbol: typing.Union[MetaOapg.properties.systemSymbol, str, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, ],
        type: 'WaypointType',
        orbitals: typing.Union[MetaOapg.properties.orbitals, list, tuple, ],
        faction: typing.Union['WaypointFaction', schemas.Unset] = schemas.unset,
        chart: typing.Union['Chart', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Waypoint':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            traits=traits,
            systemSymbol=systemSymbol,
            x=x,
            y=y,
            type=type,
            orbitals=orbitals,
            faction=faction,
            chart=chart,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.chart import Chart
from openapi_client.model.waypoint_faction import WaypointFaction
from openapi_client.model.waypoint_orbital import WaypointOrbital
from openapi_client.model.waypoint_trait import WaypointTrait
from openapi_client.model.waypoint_type import WaypointType
