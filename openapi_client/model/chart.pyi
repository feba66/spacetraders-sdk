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


class Chart(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The chart of a system or waypoint, which makes the location visible to other agents.
    """


    class MetaOapg:
        
        class properties:
            submittedBy = schemas.StrSchema
            submittedOn = schemas.DateTimeSchema
            __annotations__ = {
                "submittedBy": submittedBy,
                "submittedOn": submittedOn,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedBy"]) -> MetaOapg.properties.submittedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedOn"]) -> MetaOapg.properties.submittedOn: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["submittedBy", "submittedOn", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedBy"]) -> typing.Union[MetaOapg.properties.submittedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedOn"]) -> typing.Union[MetaOapg.properties.submittedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["submittedBy", "submittedOn", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        submittedBy: typing.Union[MetaOapg.properties.submittedBy, str, schemas.Unset] = schemas.unset,
        submittedOn: typing.Union[MetaOapg.properties.submittedOn, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Chart':
        return super().__new__(
            cls,
            *args,
            submittedBy=submittedBy,
            submittedOn=submittedOn,
            _configuration=_configuration,
            **kwargs,
        )
