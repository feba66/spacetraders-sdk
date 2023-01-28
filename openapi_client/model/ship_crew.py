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


class ShipCrew(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The ship's crew service and maintain the ship's systems and equipment.
    """


    class MetaOapg:
        required = {
            "wages",
            "current",
            "rotation",
            "morale",
            "required",
            "capacity",
        }
        
        class properties:
            current = schemas.IntSchema
            required = schemas.IntSchema
            capacity = schemas.IntSchema
            
            
            class rotation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "STRICT": "STRICT",
                        "RELAXED": "RELAXED",
                    }
                
                @schemas.classproperty
                def STRICT(cls):
                    return cls("STRICT")
                
                @schemas.classproperty
                def RELAXED(cls):
                    return cls("RELAXED")
            
            
            class morale(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
            class wages(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            __annotations__ = {
                "current": current,
                "required": required,
                "capacity": capacity,
                "rotation": rotation,
                "morale": morale,
                "wages": wages,
            }
    
    wages: MetaOapg.properties.wages
    current: MetaOapg.properties.current
    rotation: MetaOapg.properties.rotation
    morale: MetaOapg.properties.morale
    required: MetaOapg.properties.required
    capacity: MetaOapg.properties.capacity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rotation"]) -> MetaOapg.properties.rotation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["morale"]) -> MetaOapg.properties.morale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wages"]) -> MetaOapg.properties.wages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current", "required", "capacity", "rotation", "morale", "wages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rotation"]) -> MetaOapg.properties.rotation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["morale"]) -> MetaOapg.properties.morale: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wages"]) -> MetaOapg.properties.wages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current", "required", "capacity", "rotation", "morale", "wages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        wages: typing.Union[MetaOapg.properties.wages, decimal.Decimal, int, ],
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, ],
        rotation: typing.Union[MetaOapg.properties.rotation, str, ],
        morale: typing.Union[MetaOapg.properties.morale, decimal.Decimal, int, ],
        required: typing.Union[MetaOapg.properties.required, decimal.Decimal, int, ],
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShipCrew':
        return super().__new__(
            cls,
            *args,
            wages=wages,
            current=current,
            rotation=rotation,
            morale=morale,
            required=required,
            capacity=capacity,
            _configuration=_configuration,
            **kwargs,
        )
