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


class Extraction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "yield",
            "shipSymbol",
        }
        
        class properties:
            
            
            class shipSymbol(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def _yield() -> typing.Type['ExtractionYield']:
                return ExtractionYield
            __annotations__ = {
                "shipSymbol": shipSymbol,
                "yield": _yield,
            }
    
    shipSymbol: MetaOapg.properties.shipSymbol
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yield"]) -> 'ExtractionYield': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shipSymbol", "yield", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipSymbol"]) -> MetaOapg.properties.shipSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yield"]) -> 'ExtractionYield': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shipSymbol", "yield", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shipSymbol: typing.Union[MetaOapg.properties.shipSymbol, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Extraction':
        return super().__new__(
            cls,
            *args,
            shipSymbol=shipSymbol,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.extraction_yield import ExtractionYield
