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


class Contract(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "terms",
            "factionSymbol",
            "fulfilled",
            "accepted",
            "expiration",
            "id",
            "type",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class factionSymbol(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PROCUREMENT": "PROCUREMENT",
                        "TRANSPORT": "TRANSPORT",
                        "SHUTTLE": "SHUTTLE",
                    }
                
                @schemas.classproperty
                def PROCUREMENT(cls):
                    return cls("PROCUREMENT")
                
                @schemas.classproperty
                def TRANSPORT(cls):
                    return cls("TRANSPORT")
                
                @schemas.classproperty
                def SHUTTLE(cls):
                    return cls("SHUTTLE")
        
            @staticmethod
            def terms() -> typing.Type['ContractTerms']:
                return ContractTerms
            accepted = schemas.BoolSchema
            fulfilled = schemas.BoolSchema
            expiration = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "factionSymbol": factionSymbol,
                "type": type,
                "terms": terms,
                "accepted": accepted,
                "fulfilled": fulfilled,
                "expiration": expiration,
            }
    
    terms: 'ContractTerms'
    factionSymbol: MetaOapg.properties.factionSymbol
    fulfilled: MetaOapg.properties.fulfilled
    accepted: MetaOapg.properties.accepted
    expiration: MetaOapg.properties.expiration
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factionSymbol"]) -> MetaOapg.properties.factionSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms"]) -> 'ContractTerms': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accepted"]) -> MetaOapg.properties.accepted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fulfilled"]) -> MetaOapg.properties.fulfilled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "factionSymbol", "type", "terms", "accepted", "fulfilled", "expiration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factionSymbol"]) -> MetaOapg.properties.factionSymbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms"]) -> 'ContractTerms': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accepted"]) -> MetaOapg.properties.accepted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fulfilled"]) -> MetaOapg.properties.fulfilled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "factionSymbol", "type", "terms", "accepted", "fulfilled", "expiration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        terms: 'ContractTerms',
        factionSymbol: typing.Union[MetaOapg.properties.factionSymbol, str, ],
        fulfilled: typing.Union[MetaOapg.properties.fulfilled, bool, ],
        accepted: typing.Union[MetaOapg.properties.accepted, bool, ],
        expiration: typing.Union[MetaOapg.properties.expiration, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contract':
        return super().__new__(
            cls,
            *args,
            terms=terms,
            factionSymbol=factionSymbol,
            fulfilled=fulfilled,
            accepted=accepted,
            expiration=expiration,
            id=id,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.contract_terms import ContractTerms
