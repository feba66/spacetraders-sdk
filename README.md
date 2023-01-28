# openapi-client
SpaceTraders is a multiplayer sci-fi strategy game where you acquire and manage a fleet of ships across a growing and dynamic universe.

Similar to games such as Eve Online, you work with or against other players to establish trade routes, chart new systems, mine precious ores, patrol for pirates, spy on factions, and discover hidden treasures.

SpaceTraders as a game is unique in that it is entirely accessible through open and well-documented API endpoints.

If this sounds fun and interesting to you, please drop into our Discord and get to know the community. We are actively working on new clients, new ideas and sharing tips for how to play the game.


```json http
{
  \"method\": \"GET\",
  \"url\": \"https://v2.api.spacetraders.io\",
}
```

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api
from openapi_client.model.agent import Agent
# Defining the host is optional and defaults to https://v2.api.spacetraders.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://v2.api.spacetraders.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: AgentToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    
    try:
        # My Agent Details
        api_response = api_instance.get_my_agent()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://v2.api.spacetraders.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**get_my_agent**](docs/apis/tags/AgentsApi.md#get_my_agent) | **get** /my/agent | My Agent Details
*ContractsApi* | [**accept_contract**](docs/apis/tags/ContractsApi.md#accept_contract) | **post** /my/contracts/{contractId}/accept | Accept Contract
*ContractsApi* | [**deliver_contract**](docs/apis/tags/ContractsApi.md#deliver_contract) | **post** /my/contracts/{contractId}/deliver | Deliver Contract
*ContractsApi* | [**fulfill_contract**](docs/apis/tags/ContractsApi.md#fulfill_contract) | **post** /my/contracts/{contractId}/fulfill | Fulfill Contract
*ContractsApi* | [**get_contract**](docs/apis/tags/ContractsApi.md#get_contract) | **get** /my/contracts/{contractId} | Get Contract
*ContractsApi* | [**get_contracts**](docs/apis/tags/ContractsApi.md#get_contracts) | **get** /my/contracts | List Contracts
*DefaultApi* | [**register**](docs/apis/tags/DefaultApi.md#register) | **post** /register | Register New Agent
*FactionsApi* | [**get_faction**](docs/apis/tags/FactionsApi.md#get_faction) | **get** /factions/{factionSymbol} | Get Faction
*FactionsApi* | [**get_factions**](docs/apis/tags/FactionsApi.md#get_factions) | **get** /factions | List Factions
*FleetApi* | [**create_chart**](docs/apis/tags/FleetApi.md#create_chart) | **post** /my/ships/{shipSymbol}/chart | Create Chart
*FleetApi* | [**create_ship_ship_scan**](docs/apis/tags/FleetApi.md#create_ship_ship_scan) | **post** /my/ships/{shipSymbol}/scan/ships | Scan Ships
*FleetApi* | [**create_ship_system_scan**](docs/apis/tags/FleetApi.md#create_ship_system_scan) | **post** /my/ships/{shipSymbol}/scan/systems | Scan Systems
*FleetApi* | [**create_survey**](docs/apis/tags/FleetApi.md#create_survey) | **post** /my/ships/{shipSymbol}/survey | Create Survey
*FleetApi* | [**dock_ship**](docs/apis/tags/FleetApi.md#dock_ship) | **post** /my/ships/{shipSymbol}/dock | Dock Ship
*FleetApi* | [**extract_resources**](docs/apis/tags/FleetApi.md#extract_resources) | **post** /my/ships/{shipSymbol}/extract | Extract Resources
*FleetApi* | [**get_my_ship**](docs/apis/tags/FleetApi.md#get_my_ship) | **get** /my/ships/{shipSymbol} | Get Ship
*FleetApi* | [**get_my_ships**](docs/apis/tags/FleetApi.md#get_my_ships) | **get** /my/ships | List Ships
*FleetApi* | [**get_ship_cooldown**](docs/apis/tags/FleetApi.md#get_ship_cooldown) | **get** /my/ships/{shipSymbol}/cooldown | Get Ship Cooldown
*FleetApi* | [**jettison**](docs/apis/tags/FleetApi.md#jettison) | **post** /my/ships/{shipSymbol}/jettison | Jettison Cargo
*FleetApi* | [**jump_ship**](docs/apis/tags/FleetApi.md#jump_ship) | **post** /my/ships/{shipSymbol}/jump | Jump Ship
*FleetApi* | [**navigate_ship**](docs/apis/tags/FleetApi.md#navigate_ship) | **post** /my/ships/{shipSymbol}/navigate | Navigate Ship
*FleetApi* | [**orbit_ship**](docs/apis/tags/FleetApi.md#orbit_ship) | **post** /my/ships/{shipSymbol}/orbit | Orbit Ship
*FleetApi* | [**purchase_cargo**](docs/apis/tags/FleetApi.md#purchase_cargo) | **post** /my/ships/{shipSymbol}/purchase | Purchase Cargo
*FleetApi* | [**purchase_ship**](docs/apis/tags/FleetApi.md#purchase_ship) | **post** /my/ships | Purchase Ship
*FleetApi* | [**refuel_ship**](docs/apis/tags/FleetApi.md#refuel_ship) | **post** /my/ships/{shipSymbol}/refuel | Refuel Ship
*FleetApi* | [**sell_cargo**](docs/apis/tags/FleetApi.md#sell_cargo) | **post** /my/ships/{shipSymbol}/sell | Sell Cargo
*FleetApi* | [**ship_refine**](docs/apis/tags/FleetApi.md#ship_refine) | **post** /my/ships/{shipSymbol}/refine | Ship Refine
*FleetApi* | [**transfer_cargo**](docs/apis/tags/FleetApi.md#transfer_cargo) | **post** /my/ships/{shipSymbol}/transfer | Transfer Cargo
*FleetApi* | [**warp_ship**](docs/apis/tags/FleetApi.md#warp_ship) | **post** /my/ships/{shipSymbol}/warp | Warp Ship
*SystemsApi* | [**get_jump_gate**](docs/apis/tags/SystemsApi.md#get_jump_gate) | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate | Get Jump Gate
*SystemsApi* | [**get_market**](docs/apis/tags/SystemsApi.md#get_market) | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/market | Get Market
*SystemsApi* | [**get_shipyard**](docs/apis/tags/SystemsApi.md#get_shipyard) | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard | Get Shipyard
*SystemsApi* | [**get_system**](docs/apis/tags/SystemsApi.md#get_system) | **get** /systems/{systemSymbol} | Get System
*SystemsApi* | [**get_system_waypoints**](docs/apis/tags/SystemsApi.md#get_system_waypoints) | **get** /systems/{systemSymbol}/waypoints | List Waypoints
*SystemsApi* | [**get_systems**](docs/apis/tags/SystemsApi.md#get_systems) | **get** /systems | List Systems
*SystemsApi* | [**get_waypoint**](docs/apis/tags/SystemsApi.md#get_waypoint) | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol} | Get Waypoint

## Documentation For Models

 - [Agent](docs/models/Agent.md)
 - [Chart](docs/models/Chart.md)
 - [ConnectedSystem](docs/models/ConnectedSystem.md)
 - [Contract](docs/models/Contract.md)
 - [ContractDeliverGood](docs/models/ContractDeliverGood.md)
 - [ContractPayment](docs/models/ContractPayment.md)
 - [ContractTerms](docs/models/ContractTerms.md)
 - [Cooldown](docs/models/Cooldown.md)
 - [Extraction](docs/models/Extraction.md)
 - [ExtractionYield](docs/models/ExtractionYield.md)
 - [Faction](docs/models/Faction.md)
 - [FactionTrait](docs/models/FactionTrait.md)
 - [JumpGate](docs/models/JumpGate.md)
 - [Market](docs/models/Market.md)
 - [MarketTradeGood](docs/models/MarketTradeGood.md)
 - [MarketTransaction](docs/models/MarketTransaction.md)
 - [Meta](docs/models/Meta.md)
 - [ScannedShip](docs/models/ScannedShip.md)
 - [ScannedSystem](docs/models/ScannedSystem.md)
 - [Ship](docs/models/Ship.md)
 - [ShipCargo](docs/models/ShipCargo.md)
 - [ShipCargoItem](docs/models/ShipCargoItem.md)
 - [ShipCondition](docs/models/ShipCondition.md)
 - [ShipCrew](docs/models/ShipCrew.md)
 - [ShipEngine](docs/models/ShipEngine.md)
 - [ShipFrame](docs/models/ShipFrame.md)
 - [ShipFuel](docs/models/ShipFuel.md)
 - [ShipModule](docs/models/ShipModule.md)
 - [ShipMount](docs/models/ShipMount.md)
 - [ShipNav](docs/models/ShipNav.md)
 - [ShipNavFlightMode](docs/models/ShipNavFlightMode.md)
 - [ShipNavRoute](docs/models/ShipNavRoute.md)
 - [ShipNavRouteWaypoint](docs/models/ShipNavRouteWaypoint.md)
 - [ShipNavStatus](docs/models/ShipNavStatus.md)
 - [ShipReactor](docs/models/ShipReactor.md)
 - [ShipRegistration](docs/models/ShipRegistration.md)
 - [ShipRequirements](docs/models/ShipRequirements.md)
 - [ShipRole](docs/models/ShipRole.md)
 - [ShipType](docs/models/ShipType.md)
 - [Shipyard](docs/models/Shipyard.md)
 - [ShipyardShip](docs/models/ShipyardShip.md)
 - [ShipyardTransaction](docs/models/ShipyardTransaction.md)
 - [Survey](docs/models/Survey.md)
 - [SurveyDeposit](docs/models/SurveyDeposit.md)
 - [System](docs/models/System.md)
 - [SystemFaction](docs/models/SystemFaction.md)
 - [SystemType](docs/models/SystemType.md)
 - [SystemWaypoint](docs/models/SystemWaypoint.md)
 - [TradeGood](docs/models/TradeGood.md)
 - [TradeSymbol](docs/models/TradeSymbol.md)
 - [Waypoint](docs/models/Waypoint.md)
 - [WaypointFaction](docs/models/WaypointFaction.md)
 - [WaypointOrbital](docs/models/WaypointOrbital.md)
 - [WaypointTrait](docs/models/WaypointTrait.md)
 - [WaypointType](docs/models/WaypointType.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## AgentToken

- **Type**: Bearer authentication


## Author

joel@spacetraders.io
joel@spacetraders.io
joel@spacetraders.io
joel@spacetraders.io
joel@spacetraders.io
joel@spacetraders.io

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
