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


class ContractTerms(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "payment",
            "deadline",
        }
        
        class properties:
            deadline = schemas.DateTimeSchema
        
            @staticmethod
            def payment() -> typing.Type['ContractPayment']:
                return ContractPayment
            
            
            class deliver(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContractDeliverGood']:
                        return ContractDeliverGood
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContractDeliverGood'], typing.List['ContractDeliverGood']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deliver':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContractDeliverGood':
                    return super().__getitem__(i)
            __annotations__ = {
                "deadline": deadline,
                "payment": payment,
                "deliver": deliver,
            }
    
    payment: 'ContractPayment'
    deadline: MetaOapg.properties.deadline
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deadline"]) -> MetaOapg.properties.deadline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> 'ContractPayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver"]) -> MetaOapg.properties.deliver: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["deadline", "payment", "deliver", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deadline"]) -> MetaOapg.properties.deadline: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> 'ContractPayment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver"]) -> typing.Union[MetaOapg.properties.deliver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deadline", "payment", "deliver", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payment: 'ContractPayment',
        deadline: typing.Union[MetaOapg.properties.deadline, str, datetime, ],
        deliver: typing.Union[MetaOapg.properties.deliver, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractTerms':
        return super().__new__(
            cls,
            *args,
            payment=payment,
            deadline=deadline,
            deliver=deliver,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.contract_deliver_good import ContractDeliverGood
from openapi_client.model.contract_payment import ContractPayment
