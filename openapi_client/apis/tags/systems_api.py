# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is a multiplayer sci-fi strategy game where you acquire and manage a fleet of ships across a growing and dynamic universe.  Similar to games such as Eve Online, you work with or against other players to establish trade routes, chart new systems, mine precious ores, patrol for pirates, spy on factions, and discover hidden treasures.  SpaceTraders as a game is unique in that it is entirely accessible through open and well-documented API endpoints.  If this sounds fun and interesting to you, please drop into our Discord and get to know the community. We are actively working on new clients, new ideas and sharing tips for how to play the game.   ```json http {   \"method\": \"GET\",   \"url\": \"https://api-server-2-0-0-rc-2-vxxwq5xqdq-uc.a.run.app\", } ```  # noqa: E501

    The version of the OpenAPI document: 2.0.0-rc.2
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.systems_system_symbol_waypoints_waypoint_symbol_market.get import GetMarket
from openapi_client.paths.systems_system_symbol_waypoints_waypoint_symbol_shipyard.get import GetShipyard
from openapi_client.paths.systems_system_symbol.get import GetSystem
from openapi_client.paths.systems_system_symbol_waypoints.get import GetSystemWaypoints
from openapi_client.paths.systems.get import GetSystems
from openapi_client.paths.systems_system_symbol_waypoints_waypoint_symbol.get import GetWaypoint


class SystemsApi(
    GetMarket,
    GetShipyard,
    GetSystem,
    GetSystemWaypoints,
    GetSystems,
    GetWaypoint,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
