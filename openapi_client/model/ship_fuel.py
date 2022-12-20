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


class ShipFuel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.
    """


    class MetaOapg:
        required = {
            "current",
            "capacity",
        }
        
        class properties:
            
            
            class current(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class capacity(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class consumed(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "amount",
                        "timestamp",
                    }
                    
                    class properties:
                        
                        
                        class amount(
                            schemas.IntSchema
                        ):
                        
                        
                            class MetaOapg:
                                inclusive_minimum = 0
                        timestamp = schemas.DateTimeSchema
                        __annotations__ = {
                            "amount": amount,
                            "timestamp": timestamp,
                        }
                
                amount: MetaOapg.properties.amount
                timestamp: MetaOapg.properties.timestamp
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "timestamp", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "timestamp", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
                    timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'consumed':
                    return super().__new__(
                        cls,
                        *args,
                        amount=amount,
                        timestamp=timestamp,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "current": current,
                "capacity": capacity,
                "consumed": consumed,
            }
    
    current: MetaOapg.properties.current
    capacity: MetaOapg.properties.capacity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consumed"]) -> MetaOapg.properties.consumed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current", "capacity", "consumed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consumed"]) -> typing.Union[MetaOapg.properties.consumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current", "capacity", "consumed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, ],
        consumed: typing.Union[MetaOapg.properties.consumed, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipFuel':
        return super().__new__(
            cls,
            *args,
            current=current,
            capacity=capacity,
            consumed=consumed,
            _configuration=_configuration,
            **kwargs,
        )
