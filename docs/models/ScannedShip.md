# openapi_client.model.scanned_ship.ScannedShip

The ship that was scanned. Details include information about the ship that could be detected by the scanner.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The ship that was scanned. Details include information about the ship that could be detected by the scanner. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The globally unique identifier of the ship in the following format: &#x60;[AGENT_SYMBOL]_[HEX_ID]&#x60; | 
**nav** | [**ShipNav**](ShipNav.md) | [**ShipNav**](ShipNav.md) |  | 
**engine** | [**ShipEngine**](ShipEngine.md) | [**ShipEngine**](ShipEngine.md) |  | 
**reactor** | [**ShipReactor**](ShipReactor.md) | [**ShipReactor**](ShipReactor.md) |  | 
**[mounts](#mounts)** | list, tuple,  | tuple,  |  | 
**registration** | [**ShipRegistration**](ShipRegistration.md) | [**ShipRegistration**](ShipRegistration.md) |  | 
**frame** | [**ShipFrame**](ShipFrame.md) | [**ShipFrame**](ShipFrame.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

