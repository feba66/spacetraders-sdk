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


class SystemType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of waypoint.
    """
    
    @schemas.classproperty
    def NEUTRON_STAR(cls):
        return cls("NEUTRON_STAR")
    
    @schemas.classproperty
    def RED_STAR(cls):
        return cls("RED_STAR")
    
    @schemas.classproperty
    def ORANGE_STAR(cls):
        return cls("ORANGE_STAR")
    
    @schemas.classproperty
    def BLUE_STAR(cls):
        return cls("BLUE_STAR")
    
    @schemas.classproperty
    def YOUNG_STAR(cls):
        return cls("YOUNG_STAR")
    
    @schemas.classproperty
    def WHITE_DWARF(cls):
        return cls("WHITE_DWARF")
    
    @schemas.classproperty
    def BLACK_HOLE(cls):
        return cls("BLACK_HOLE")
    
    @schemas.classproperty
    def HYPERGIANT(cls):
        return cls("HYPERGIANT")
    
    @schemas.classproperty
    def NEBULA(cls):
        return cls("NEBULA")
    
    @schemas.classproperty
    def UNSTABLE(cls):
        return cls("UNSTABLE")
