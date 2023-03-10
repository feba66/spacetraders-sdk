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


class Ship(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A ship
    """


    class MetaOapg:
        required = {
            "symbol",
            "nav",
            "engine",
            "fuel",
            "reactor",
            "mounts",
            "registration",
            "cargo",
            "modules",
            "crew",
            "frame",
        }
        
        class properties:
            
            
            class symbol(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 8
        
            @staticmethod
            def registration() -> typing.Type['ShipRegistration']:
                return ShipRegistration
        
            @staticmethod
            def nav() -> typing.Type['ShipNav']:
                return ShipNav
        
            @staticmethod
            def crew() -> typing.Type['ShipCrew']:
                return ShipCrew
        
            @staticmethod
            def frame() -> typing.Type['ShipFrame']:
                return ShipFrame
        
            @staticmethod
            def reactor() -> typing.Type['ShipReactor']:
                return ShipReactor
        
            @staticmethod
            def engine() -> typing.Type['ShipEngine']:
                return ShipEngine
            
            
            class modules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShipModule']:
                        return ShipModule
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ShipModule'], typing.List['ShipModule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modules':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShipModule':
                    return super().__getitem__(i)
            
            
            class mounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShipMount']:
                        return ShipMount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ShipMount'], typing.List['ShipMount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mounts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShipMount':
                    return super().__getitem__(i)
        
            @staticmethod
            def cargo() -> typing.Type['ShipCargo']:
                return ShipCargo
        
            @staticmethod
            def fuel() -> typing.Type['ShipFuel']:
                return ShipFuel
            __annotations__ = {
                "symbol": symbol,
                "registration": registration,
                "nav": nav,
                "crew": crew,
                "frame": frame,
                "reactor": reactor,
                "engine": engine,
                "modules": modules,
                "mounts": mounts,
                "cargo": cargo,
                "fuel": fuel,
            }
    
    symbol: MetaOapg.properties.symbol
    nav: 'ShipNav'
    engine: 'ShipEngine'
    fuel: 'ShipFuel'
    reactor: 'ShipReactor'
    mounts: MetaOapg.properties.mounts
    registration: 'ShipRegistration'
    cargo: 'ShipCargo'
    modules: MetaOapg.properties.modules
    crew: 'ShipCrew'
    frame: 'ShipFrame'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration"]) -> 'ShipRegistration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nav"]) -> 'ShipNav': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crew"]) -> 'ShipCrew': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frame"]) -> 'ShipFrame': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactor"]) -> 'ShipReactor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engine"]) -> 'ShipEngine': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modules"]) -> MetaOapg.properties.modules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mounts"]) -> MetaOapg.properties.mounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cargo"]) -> 'ShipCargo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fuel"]) -> 'ShipFuel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "registration", "nav", "crew", "frame", "reactor", "engine", "modules", "mounts", "cargo", "fuel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration"]) -> 'ShipRegistration': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nav"]) -> 'ShipNav': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crew"]) -> 'ShipCrew': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frame"]) -> 'ShipFrame': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactor"]) -> 'ShipReactor': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engine"]) -> 'ShipEngine': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modules"]) -> MetaOapg.properties.modules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mounts"]) -> MetaOapg.properties.mounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cargo"]) -> 'ShipCargo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fuel"]) -> 'ShipFuel': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "registration", "nav", "crew", "frame", "reactor", "engine", "modules", "mounts", "cargo", "fuel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        nav: 'ShipNav',
        engine: 'ShipEngine',
        fuel: 'ShipFuel',
        reactor: 'ShipReactor',
        mounts: typing.Union[MetaOapg.properties.mounts, list, tuple, ],
        registration: 'ShipRegistration',
        cargo: 'ShipCargo',
        modules: typing.Union[MetaOapg.properties.modules, list, tuple, ],
        crew: 'ShipCrew',
        frame: 'ShipFrame',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Ship':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            nav=nav,
            engine=engine,
            fuel=fuel,
            reactor=reactor,
            mounts=mounts,
            registration=registration,
            cargo=cargo,
            modules=modules,
            crew=crew,
            frame=frame,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.ship_cargo import ShipCargo
from openapi_client.model.ship_crew import ShipCrew
from openapi_client.model.ship_engine import ShipEngine
from openapi_client.model.ship_frame import ShipFrame
from openapi_client.model.ship_fuel import ShipFuel
from openapi_client.model.ship_module import ShipModule
from openapi_client.model.ship_mount import ShipMount
from openapi_client.model.ship_nav import ShipNav
from openapi_client.model.ship_reactor import ShipReactor
from openapi_client.model.ship_registration import ShipRegistration
