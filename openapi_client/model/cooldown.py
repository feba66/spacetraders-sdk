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


class Cooldown(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A cooldown is a period of time in which a ship cannot perform certain actions.
    """


    class MetaOapg:
        required = {
            "remainingSeconds",
            "totalSeconds",
            "expiration",
            "shipSymbol",
        }
        
        class properties:
            
            
            class shipSymbol(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class totalSeconds(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class remainingSeconds(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class expiration(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            __annotations__ = {
                "shipSymbol": shipSymbol,
                "totalSeconds": totalSeconds,
                "remainingSeconds": remainingSeconds,
                "expiration": expiration,
            }
    
    remainingSeconds: MetaOapg.properties.remainingSeconds
    totalSeconds: MetaOapg.properties.totalSeconds
    expiration: MetaOapg.properties.expiration
    shipSymbol: MetaOapg.properties.shipSymbol
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalSeconds"]) -> MetaOapg.properties.totalSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remainingSeconds"]) -> MetaOapg.properties.remainingSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shipSymbol", "totalSeconds", "remainingSeconds", "expiration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalSeconds"]) -> MetaOapg.properties.totalSeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remainingSeconds"]) -> MetaOapg.properties.remainingSeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shipSymbol", "totalSeconds", "remainingSeconds", "expiration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        remainingSeconds: typing.Union[MetaOapg.properties.remainingSeconds, decimal.Decimal, int, ],
        totalSeconds: typing.Union[MetaOapg.properties.totalSeconds, decimal.Decimal, int, ],
        expiration: typing.Union[MetaOapg.properties.expiration, str, datetime, ],
        shipSymbol: typing.Union[MetaOapg.properties.shipSymbol, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Cooldown':
        return super().__new__(
            cls,
            *args,
            remainingSeconds=remainingSeconds,
            totalSeconds=totalSeconds,
            expiration=expiration,
            shipSymbol=shipSymbol,
            _configuration=_configuration,
            **kwargs,
        )
