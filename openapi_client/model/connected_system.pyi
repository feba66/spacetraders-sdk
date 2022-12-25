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


class ConnectedSystem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "distance",
            "sectorSymbol",
            "x",
            "y",
            "type",
        }
        
        class properties:
            
            
            class symbol(
                schemas.StrSchema
            ):
                pass
            
            
            class sectorSymbol(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def type() -> typing.Type['SystemType']:
                return SystemType
            x = schemas.IntSchema
            y = schemas.IntSchema
            distance = schemas.IntSchema
            factionSymbol = schemas.StrSchema
            __annotations__ = {
                "symbol": symbol,
                "sectorSymbol": sectorSymbol,
                "type": type,
                "x": x,
                "y": y,
                "distance": distance,
                "factionSymbol": factionSymbol,
            }
    
    symbol: MetaOapg.properties.symbol
    distance: MetaOapg.properties.distance
    sectorSymbol: MetaOapg.properties.sectorSymbol
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    type: 'SystemType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sectorSymbol"]) -> MetaOapg.properties.sectorSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'SystemType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distance"]) -> MetaOapg.properties.distance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factionSymbol"]) -> MetaOapg.properties.factionSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "sectorSymbol", "type", "x", "y", "distance", "factionSymbol", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sectorSymbol"]) -> MetaOapg.properties.sectorSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'SystemType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distance"]) -> MetaOapg.properties.distance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factionSymbol"]) -> typing.Union[MetaOapg.properties.factionSymbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "sectorSymbol", "type", "x", "y", "distance", "factionSymbol", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        distance: typing.Union[MetaOapg.properties.distance, decimal.Decimal, int, ],
        sectorSymbol: typing.Union[MetaOapg.properties.sectorSymbol, str, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, ],
        type: 'SystemType',
        factionSymbol: typing.Union[MetaOapg.properties.factionSymbol, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectedSystem':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            distance=distance,
            sectorSymbol=sectorSymbol,
            x=x,
            y=y,
            type=type,
            factionSymbol=factionSymbol,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.system_type import SystemType
