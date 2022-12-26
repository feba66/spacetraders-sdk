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


class MarketTradeGood(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tradeVolume",
            "symbol",
            "sellPrice",
            "purchasePrice",
            "supply",
        }
        
        class properties:
            symbol = schemas.StrSchema
            
            
            class tradeVolume(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 1
            
            
            class supply(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SCARCE": "SCARCE",
                        "LIMITED": "LIMITED",
                        "MODERATE": "MODERATE",
                        "ABUNDANT": "ABUNDANT",
                    }
                
                @schemas.classproperty
                def SCARCE(cls):
                    return cls("SCARCE")
                
                @schemas.classproperty
                def LIMITED(cls):
                    return cls("LIMITED")
                
                @schemas.classproperty
                def MODERATE(cls):
                    return cls("MODERATE")
                
                @schemas.classproperty
                def ABUNDANT(cls):
                    return cls("ABUNDANT")
            
            
            class purchasePrice(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class sellPrice(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            __annotations__ = {
                "symbol": symbol,
                "tradeVolume": tradeVolume,
                "supply": supply,
                "purchasePrice": purchasePrice,
                "sellPrice": sellPrice,
            }
    
    tradeVolume: MetaOapg.properties.tradeVolume
    symbol: MetaOapg.properties.symbol
    sellPrice: MetaOapg.properties.sellPrice
    purchasePrice: MetaOapg.properties.purchasePrice
    supply: MetaOapg.properties.supply
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradeVolume"]) -> MetaOapg.properties.tradeVolume: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supply"]) -> MetaOapg.properties.supply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchasePrice"]) -> MetaOapg.properties.purchasePrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sellPrice"]) -> MetaOapg.properties.sellPrice: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "tradeVolume", "supply", "purchasePrice", "sellPrice", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradeVolume"]) -> MetaOapg.properties.tradeVolume: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supply"]) -> MetaOapg.properties.supply: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchasePrice"]) -> MetaOapg.properties.purchasePrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sellPrice"]) -> MetaOapg.properties.sellPrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "tradeVolume", "supply", "purchasePrice", "sellPrice", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tradeVolume: typing.Union[MetaOapg.properties.tradeVolume, decimal.Decimal, int, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        sellPrice: typing.Union[MetaOapg.properties.sellPrice, decimal.Decimal, int, ],
        purchasePrice: typing.Union[MetaOapg.properties.purchasePrice, decimal.Decimal, int, ],
        supply: typing.Union[MetaOapg.properties.supply, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketTradeGood':
        return super().__new__(
            cls,
            *args,
            tradeVolume=tradeVolume,
            symbol=symbol,
            sellPrice=sellPrice,
            purchasePrice=purchasePrice,
            supply=supply,
            _configuration=_configuration,
            **kwargs,
        )
