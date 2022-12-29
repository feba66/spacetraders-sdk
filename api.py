
from datetime import datetime
import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import agents_api, contracts_api, default_api, factions_api, fleet_api, systems_api
from classes_n_enums import *
import json

PATH_PREFIX = "spacetraders-sdk/"

class SpaceTraders:
    api_client: openapi_client.ApiClient

    api_agents = agents_api.AgentsApi
    api_contracts = contracts_api.ContractsApi
    def_api = default_api.DefaultApi
    api_factions = factions_api.FactionsApi
    api_fleet = fleet_api.FleetApi
    api_systems: systems_api.SystemsApi

    systems: dict[str,System]
    contracts: dict[str,Contract]
    agent: Agent
    ships: dict[str,Ship]
    cooldowns: dict[str,Cooldown]
    surveys:list[Survey]
    waypoints:dict[str,Waypoint]
    shipyards:dict[str,Shipyard]
    markets:dict[str,Market]

    def __init__(self,token=None) -> None:
        configuration = openapi_client.Configuration()
        if token == None:
            try:
                with open(PATH_PREFIX+"acc.txt", "r") as f:
                    configuration.access_token = f.readline().replace("\n", "")
            except:
                pass
        else:
            configuration.access_token = token
        self.api_client = openapi_client.ApiClient(configuration)

        self.api_agents = agents_api.AgentsApi(self.api_client)
        self.api_contracts = contracts_api.ContractsApi(self.api_client)
        self.def_api = default_api.DefaultApi(self.api_client)
        self.api_factions = factions_api.FactionsApi(self.api_client)
        self.api_fleet = fleet_api.FleetApi(self.api_client)
        self.api_systems = systems_api.SystemsApi(self.api_client)

        self.ships={}
        self.contracts={}
        self.cooldowns={}
        self.surveys=[]
        self.systems={}
        self.waypoints={}
        self.shipyards={}
    # region DefaultApi
    def register(self,name,faction):
        try:
            r = self.def_api.register(body={"symbol": name, "faction": faction})

            token = r.body["data"]["token"]
            print(token)
            with open(PATH_PREFIX+"acc.txt","a") as f:
                f.write(token+"\n")

            agent = Agent(r.body["data"]["agent"])
            contract = Contract(r.body["data"]["contract"])
            factionc = Faction(r.body["data"]["faction"])
            ship = Ship(r.body["data"]["ship"])
            pprint(agent)
            pprint(contract)
            pprint(factionc)
            pprint(ship)
            # pprint(r.response.data)
            return r
        except openapi_client.ApiException as e:
            print("Exception when calling DefaultApi->register: %s\n" % e)
    # endregion
    
    # region AgentsApi
    def get_agent(self):
        try:
            print("Get Agent")
            api_response = self.api_agents.get_my_agent()
            agent = Agent(api_response.body["data"])
            self.agent = agent
            return  agent
        except openapi_client.ApiException as e:
            print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
    # endregion
    
    # region FactionsApi
    def get_factions(self):
        try:
            api_response = self.api_factions.get_factions()
            return [Faction(f) for f in api_response.body["data"]]
        except openapi_client.ApiException as e:
            print("Exception when calling FactionsApi->get_factions: %s\n" % e)
    def get_faction(self,factionSymbol):
        try:
            api_response = self.api_factions.get_faction(path_params={"factionSymbol": factionSymbol})
            return Faction(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling FactionsApi->get_faction: %s\n" % e)
    # endregion
    
    # region ContractsApi
    def accept_contract(self, contractId):
        try:
            api_response = self.api_contracts.accept_contract(path_params={"contractId": contractId})
            a,c =(Agent(api_response.body["data"]["agent"]),Contract(api_response.body["data"]["contract"]))
            self.agent = a
            self.contracts[c.id]=c
            return (a,c)
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->accept_contract: %s\n" % e)
    def deliver_contract(self, contractId, shipSymbol, tradeSymbol, units):
        try:
            api_response = self.api_contracts.deliver_contract(path_params={"contractId": contractId}, body={"tradeSymbol": tradeSymbol, "shipSymbol": shipSymbol, "units": units})
            co, ca =(Contract(api_response.body["data"]["contract"]),ShipCargo(api_response.body["data"]["cargo"]))
            self.ships[shipSymbol].cargo = ca
            self.contracts[co.id]=co
            return (co,ca)
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->deliver_contract: %s\n" % e)

    def get_contract(self,contractId):
        try:
            api_response = self.api_contracts.get_contract(path_params = {"contractId": contractId})
            c = Contract(api_response.body["data"])
            self.contracts[c.id]=c
            return c
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contract: %s\n" % e)
    def get_contracts(self):
        try:
            print("Get Contracts")
            api_response = self.api_contracts.get_contracts()
            contracts = {}
            for c in [Contract(c) for c in api_response.body["data"]]:
                contracts[c.id]=c
            self.contracts=contracts
            return self.contracts
        except openapi_client.ApiException as e:
            print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
    # endregion
    
    # region FleetApi
    def create_chart(self, shipSymbol):
        try:
            api_response = self.api_fleet.create_chart(path_params={"shipSymbol": shipSymbol})
            waypoint = Waypoint(api_response.body["data"]["waypoint"])
            chart = Chart(api_response.body["data"]["chart"])
            self.waypoints[waypoint.symbol]=waypoint
            return (waypoint,chart)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->create_chart: %s\n" % e)
    
    def create_survey(self,shipSymbol):
        try:
            api_response = self.api_fleet.create_survey(path_params={"shipSymbol": shipSymbol})
            c,s = (Cooldown(api_response.body["data"]["cooldown"]),[Survey(s) for s in api_response.body["data"]["surveys"]])
            self.cooldowns[shipSymbol]=c
            self.surveys.extend(s)
            return (c,s)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->create_survey: %s\n" % e)
    def dock_ship(self,shipSymbol):
        try:
            print(f"Dock {shipSymbol}")
            api_response = self.api_fleet.dock_ship(path_params={"shipSymbol": shipSymbol})
            nav = ShipNav(api_response.body["data"]["nav"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav=nav
            return nav
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->dock_ship: %s\n" % e)
    def extract_resources(self,shipSymbol,survey=None):
        try:
            print(f"Extracting with {shipSymbol}")
            api_response = self.api_fleet.extract_resources(path_params={"shipSymbol": shipSymbol},body={"survey":survey.dict()} if survey!=None else {})
            co,ca,ex =(Cooldown(api_response.body["data"]["cooldown"]),ShipCargo(api_response.body["data"]["cargo"]),Extraction(api_response.body["data"]["extraction"]))
            self.cooldowns[shipSymbol]=co
            if shipSymbol in self.ships:
                self.ships[shipSymbol].cargo=ca
            return (co,ca,ex)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->extract_resources: %s\n" % e)
    def get_my_ship(self,shipSymbol):
        try:
            print(f"Get Ship {shipSymbol}")
            api_response = self.api_fleet.get_my_ship(path_params={"shipSymbol": shipSymbol})
            ship = Ship(api_response.body["data"])
            self.ships[ship.symbol]=ship
            return ship
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->get_my_ship: %s\n" % e)
    def get_my_ships(self):
        try:
            print("Get Ships")
            api_response = self.api_fleet.get_my_ships()
            # pprint(api_response.body["meta"])
            ships = [Ship(k) for k in api_response.body["data"]]
            for s in ships:
                self.ships[s.symbol]=s
            return ships 
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->get_my_ships: %s\n" % e)
    def get_ship_cooldown(self,shipSymbol):
        try:
            print(f"Getting cooldown of {shipSymbol}")
            api_response = self.api_fleet.get_ship_cooldown(path_params={"shipSymbol": shipSymbol})
            cooldown = Cooldown(api_response.body["data"]) 
            if shipSymbol in self.ships:
                self.cooldowns[shipSymbol]=cooldown
            return cooldown
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->get_ship_cooldown: %s\n" % e)
        except TypeError as e:
            self.cooldowns[shipSymbol]=None
            return None

    def jettison(self,shipSymbol,good,units):
        try:
            print(f"Thrown away {units}x {good} from {shipSymbol}")
            api_response = self.api_fleet.jettison(path_params={"shipSymbol": shipSymbol},body={"symbol":good,"units":units})
            cargo = ShipCargo(api_response.body["data"]["cargo"]) 
            if shipSymbol in self.ships:
                self.ships[shipSymbol].cargo=cargo
            return cargo
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->jettison: %s\n" % e)

    def navigate_ship(self,shipSymbol,waypointSymbol):
        try:
            print(f"Navigating {shipSymbol} to {waypointSymbol}")
            api_response = self.api_fleet.navigate_ship(path_params={"shipSymbol": shipSymbol},body={"waypointSymbol":waypointSymbol})
            
            nav = ShipNav(api_response.body["data"]["nav"])
            fuel = ShipFuel(api_response.body["data"]["fuel"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav = nav
                self.ships[shipSymbol].fuel = fuel
            return (nav,fuel)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->navigate_ship: %s\n" % e)
    def orbit_ship(self,shipSymbol):
        try:
            print(f"Orbit {shipSymbol}")
            api_response = self.api_fleet.orbit_ship(path_params={"shipSymbol": shipSymbol})
            nav = ShipNav(api_response.body["data"]["nav"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].nav=nav
            return nav
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->orbit_ship: %s\n" % e)
    
    def purchase_ship(self, waypointSymbol,shipType):
        try:
            api_response = self.api_fleet.purchase_ship(body={"waypointSymbol": waypointSymbol,"shipType":shipType})
            a,s=(Agent(api_response.body["data"]["agent"]),Ship(api_response.body["data"]["ship"]))
            self.agent=a
            self.ships[s.symbol]=s
            return (a,s)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->purchase_ship: %s\n" % e)
    def refuel_ship(self,shipSymbol):
        try:
            print(f"Refueling {shipSymbol}")
            api_response = self.api_fleet.refuel_ship(path_params={"shipSymbol": shipSymbol})
            a,f = (Agent(api_response.body["data"]["agent"]),ShipFuel(api_response.body["data"]["fuel"]))
            self.agent=a
            if shipSymbol in self.ships:
                self.ships[shipSymbol].fuel=f
            return (a,f)
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->refuel_ship: %s\n" % e)
    def sell_cargo(self,shipSymbol,good,units):
        try:
            api_response = self.api_fleet.sell_cargo(path_params={"shipSymbol": shipSymbol},body={"symbol":good,"units":units})
            self.agent = Agent(api_response.body["data"]["agent"])
            cargo = ShipCargo(api_response.body["data"]["cargo"])
            transaction = MarketTransaction(api_response.body["data"]["transaction"])
            if shipSymbol in self.ships:
                self.ships[shipSymbol].cargo=cargo
                
            print(f"Sold {units}x {good} from {shipSymbol}")
            return (self.agent,cargo,transaction)

        except openapi_client.ApiException as e:
            j = json.loads(str(e.body).replace("b'","").replace("}}'","}}"))
            code = j["error"]["code"]
            try:
                print(f"Failed to sell {units}x {good} from {shipSymbol}: {ErrorCodes(code)}")
            except:
                print(f"Failed to sell {units}x {good} from {shipSymbol}")
            print("Exception when calling FleetApi->sell_cargo: %s\n" % e)
    def transfer_cargo(self,shipSymbol,good,units,receivingShipSymbol):
        try:
            api_response = self.api_fleet.transfer_cargo(path_params={"shipSymbol": shipSymbol},body={"tradeSymbol":good,"units":units,"shipSymbol":receivingShipSymbol})
            return (ShipCargo(api_response.body["data"]["cargo"]))
        except openapi_client.ApiException as e:
            print("Exception when calling FleetApi->transfer_cargo: %s\n" % e)
    
    
    # endregion
    
    # region SystemsApi
    def get_waypoint(self,waypointSymbol):
        try:
            api_response = self.api_systems.get_waypoint(path_params={"systemSymbol": self.system_sym_f_wayp(waypointSymbol),"waypointSymbol":waypointSymbol})
            w = Waypoint(api_response.body["data"])
            self.waypoints[w.symbol]=w
            return w
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_waypoint: %s\n" % e)
    def get_jump_gate(self,systemSymbol,waypointSymbol):
        try:
            api_response = self.api_systems.get_jump_gate(path_params={"systemSymbol": systemSymbol,"waypointSymbol":waypointSymbol})
            return JumpGate(api_response.body["data"])
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_jump_gate: %s\n" % e)
    def get_market(self,waypointSymbol):
        try:
            api_response = self.api_systems.get_market(path_params={"systemSymbol": waypointSymbol[0:waypointSymbol.find("-",4)],"waypointSymbol":waypointSymbol})
            m = Market(api_response.body["data"])
            self.markets[m.symbol]=m
            return m
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_market: %s\n" % e)
    def get_shipyard(self,waypointSymbol):
        try:
            api_response = self.api_systems.get_shipyard(path_params={"systemSymbol": self.system_sym_f_wayp(waypointSymbol),"waypointSymbol":waypointSymbol})
            s = Shipyard(api_response.body["data"])
            self.shipyards[s.symbol]=s
            return s
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_shipyard: %s\n" % e)
    def get_system_waypoints(self,systemSymbol):
        try:
            print(f"Get {systemSymbol} Waypoints")
            api_response = self.api_systems.get_system_waypoints(path_params={"systemSymbol": systemSymbol})
            waypoints = [Waypoint(w) for w in api_response.body["data"]]
            for w in waypoints:
                self.waypoints[w.symbol]=w
            return waypoints
        except openapi_client.ApiException as e:
            print("Exception when calling SystemsApi->get_system_waypoints: %s\n" % e)
    def get_system(self,systemSymbol):
        try:
            print("Get System")
            api_response = self.api_systems.get_system(path_params={"systemSymbol": systemSymbol})
            s = System(api_response.body["data"])
            self.systems[systemSymbol]=s
            return s
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_system: %s\n" % e)
    def get_systems(self):
        try:
            print("Get Systems")
            api_response = self.api_systems.get_systems()
            with open(PATH_PREFIX+"systems.json","w") as f:
                f.write(str(api_response.response.data).replace("b'","").replace("'",""))
            for sd in api_response.body["data"]:
                s = System(sd)
                self.systems[s.symbol] = s 
            return self.systems
        except openapi_client.ApiException as e:
            print("Exception when calling SystemApi->get_systems: %s\n" % e)
    # endregion

    #region asdf
    def timestamp_to_duration(self,timestamp):
        return (datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S.%fZ") - datetime.utcnow()).total_seconds()

    def remove_survey(self,id):
        for s in self.surveys:
            if s.signature == id:
                self.surveys.remove(s)
                break
    def system_sym_f_wayp(self,waypointSymbol):
        return waypointSymbol[0:waypointSymbol.find("-",4)]
    #endregion

    #region nop
    def nop(): pass # VS Code wont let me close the last region that contains a def so this is a fix for that
    #endregion

if __name__ == "__main__":
    st = SpaceTraders()
    prices = {"SHIP_PROBE":69972,"SHIP_MINING_DRONE":87220,"SHIP_ORE_HOUND":159220,"SHIP_REFINING_FREIGHTER":1696320}
    # st.register("test0003","COSMIC")
    # pprint(st.get_factions())
    # exit()
    # pprint(st.get_agent())
    system = "X1-UV97"
    waypoint = "X1-UV97-21170Z"
    shipyardWaypoint = "X1-UV97-44217E"
    jumpWaypoint = "X1-UV97-23539X"
    ship = "FEBATE5T-1"
    drone = "FEBATE5T-2"
    asteroidField ="X1-UV97-24895D"
    contractId="clc3oyf4l000ss60j6lzyx2mv"
    contractIce ="X1-UV97-21170Z"
    copperAlu="X1-UV97-57201E"
    silverGoldPlat="X1-UV97-82653Z"
    # pprint(st.get_waypoint(system,waypoint))
    # pprint(st.get_system(system))
    # pprint(st.get_systems())
    # pprint(st.get_system_waypoints(system))
    # pprint(st.get_shipyard(system,shipyardWaypoint))
    # pprint(st.get_market(system,shipyardWaypoint))
    # pprint(st.get_jump_gate(system,jumpWaypoint))
    # pprint(st.get_contract("clc3oyf4l000ss60j6lzyx2mv"))
    # pprint(st.get_contracts())

    # pprint(st.get_my_ships())
    # pprint(st.create_chart(ship))
    # pprint(st.get_my_ship(ship))

    # pprint(st.orbit_ship(ship))
    # pprint(st.navigate_ship(ship,asteroidField))

    # cooldown,surveys=st.create_survey(ship)
    # pprint((cooldown,surveys))
    # pprint(st.dock_ship(ship))
    # time.sleep(cooldown.remainingSeconds)
    # pprint(st.extract_resources(ship,surveys[0]))
    # while True:
    #     r = st.extract_resources(ship)
    #     pprint(r)
    #     time.sleep(r[0].totalSeconds)

    # pprint(st.navigate_ship(ship,"X1-UV97-25702Z"))
    # pprint(st.get_my_ships())
    # pprint(st.sell_cargo(ship,"AMMONIA_ICE",16))
    # pprint(st.get_market(system,"X1-UV97-25702Z"))
    # waypoints = st.get_system_waypoints(system)
    # pprint(waypoints)
    # markets,shipyards=[],[]
    # for w in waypoints:
    #     print(w.symbol)
    #     if WaypointTraitSymbols.MARKETPLACE in [x.symbol for x in w.traits]:
    #         markets.append(w)
    #         m = st.get_market(system,w.symbol)
    #         pprint(([x.symbol for x in m.imports],[x.symbol for x in m.exports],[x.symbol for x in m.exchange]))
    #     if WaypointTraitSymbols.SHIPYARD in [x.symbol for x in w.traits]:
    #         shipyards.append(w)
    #         pprint(st.get_shipyard(system,w.symbol))
    # pprint(st.navigate_ship(ship,"X1-UV97-44217E"))
    # pprint(st.purchase_ship(shipyardWaypoint,"SHIP_PROBE"))

    # pprint(st.accept_contract(contractId))
    # st.orbit_ship(ship)
    # pprint(st.navigate_ship(ship,asteroidField))
    def handleCargo(shipsymbol):
        cargo = st.ships[shipsymbol].cargo
        icewaterway   = "X1-UV97-21170Z"
        ammoniaiceway = "X1-UV97-25702Z"
        contractId="clc3oyf4l000ss60j6lzyx2mv"
        inplace = [TradeSymbol.COPPER_ORE,TradeSymbol.ALUMINUM_ORE,TradeSymbol.SILVER_ORE,TradeSymbol.GOLD_ORE,TradeSymbol.PLATINUM_ORE]
        pprint([x.symbol for x in cargo.inventory])
        for good in inplace:
            print(good)
            if str(good) in [x.symbol for x in cargo.inventory]:
                st.dock_ship(shipsymbol)
                pprint(st.sell_cargo(shipsymbol,str(good),sum([x.units if x.symbol == str(good) else 0 for x in cargo.inventory]))[2])
        
        if "ICE_WATER" in [x.symbol for x in cargo.inventory] or "IRON_ORE" in [x.symbol for x in cargo.inventory]:
            st.orbit_ship(shipsymbol)
            r = st.navigate_ship(shipsymbol,icewaterway)
            pprint(r)
            t = st.timestamp_to_duration(r[0].route.arrival)
            time.sleep(t)
            st.dock_ship(shipsymbol)
            if "ICE_WATER" in [x.symbol for x in cargo.inventory]:
                pprint(st.sell_cargo(shipsymbol,"ICE_WATER",sum([x.units if x.symbol == "ICE_WATER" else 0 for x in cargo.inventory])))
            if "IRON_ORE" in [x.symbol for x in cargo.inventory]:
                pprint(st.deliver_contract(contractId,"IRON_ORE",shipsymbol,sum([x.units if x.symbol == "IRON_ORE" else 0 for x in cargo.inventory])))
        
        if "AMMONIA_ICE" in [x.symbol for x in cargo.inventory]:
            st.orbit_ship(shipsymbol)
            r = st.navigate_ship(shipsymbol,ammoniaiceway)
            pprint(r)
            t = st.timestamp_to_duration(r[0].route.arrival)
            time.sleep(t)
            st.dock_ship(shipsymbol)
            pprint(st.sell_cargo(shipsymbol,"AMMONIA_ICE",sum([x.units if x.symbol == "AMMONIA_ICE" else 0 for x in cargo.inventory])))
    def dumpunused(shipsymbol):
        cargo = st.ships[shipsymbol].cargo
        if "QUARTZ_SAND" in [x.symbol for x in cargo.inventory]:
            pprint(st.jettison(shipsymbol,"QUARTZ_SAND",sum([x.units if x.symbol == "QUARTZ_SAND" else 0 for x in cargo.inventory])))

        if "SILICON_CRYSTALS" in [x.symbol for x in cargo.inventory]:
            pprint(st.jettison(shipsymbol,"SILICON_CRYSTALS",sum([x.units if x.symbol == "SILICON_CRYSTALS" else 0 for x in cargo.inventory])))
        
    # pprint(st.get_my_ship(drone).cargo)
    # pprint(st.get_my_ship(ship).cargo)
    # handleCargo(ship,st.get_my_ship(ship).cargo)
    pprint(st.get_my_ships())
    # handleCargo(ship)

    # r = st.navigate_ship(ship,asteroidField)
    # pprint(r)
    
    # t = st.timestamp_to_duration(r[0].route.arrival)
    # time.sleep(t)

    # pprint(st.navigate_ship(ship,asteroidField))
    # pprint(st.jettison(ship,"QUARTZ_SAND",13))
    # pprint(st.get_market("X1-UV97-21170Z"))
    # pprint(st.navigate_ship(ship,"X1-UV97-25702Z"))
    # pprint(st.get_market("X1-UV97-25702Z"))
    # st.dock_ship(ship)
    # pprint(st.refuel_ship(ship))
    # pprint(st.)
    # pprint(st.transfer_cargo(ship,"ANTIMATTER",15,drone))
    # pprint(st.transfer_cargo(drone,"ICE_WATER",15,ship))

    def dumbsell(shipsymbol):
        cargo = st.ships[shipsymbol].cargo

        inplace = [TradeSymbol.IRON_ORE,TradeSymbol.COPPER_ORE,TradeSymbol.ALUMINUM_ORE,TradeSymbol.SILVER_ORE,TradeSymbol.GOLD_ORE,TradeSymbol.PLATINUM_ORE]
        for good in inplace:
            if str(good) in [x.symbol for x in cargo.inventory]:
                pprint(st.sell_cargo(shipsymbol,str(good),sum([x.units if x.symbol == str(good) else 0 for x in cargo.inventory]))[2])
        
        dump = "ICE_WATER","AMMONIA_ICE","QUARTZ_SAND","SILICON_CRYSTALS"
        for good in dump:
            if good in [x.symbol for x in cargo.inventory]:
                pprint(st.jettison(shipsymbol,good,sum([x.units if x.symbol == good else 0 for x in cargo.inventory])))
        
    
    st.dock_ship(ship)
    st.dock_ship(drone)
    # while True:
    #     dumbsell(ship)
    #     dumbsell(drone)
    #     pprint(st.extract_resources(ship)[2])
    #     pprint(st.extract_resources(drone)[2])
    # #     dumpunused(ship)
    # #     dumpunused(drone)
    #     pprint(st.agent.credits)
    #     time.sleep(60)
    # pprint(st.get_market(copperAlu))

    pprint([x.symbol for x in st.get_factions()])


    # st.dock_ship(ship)
    # pprint(st.refuel_ship(ship))
    # pprint(st.get_agent())
    # pprint(st.get_my_ship(drone))
    # pprint(st.transfer_cargo(ship,"ICE_WATER",11,drone))
    # pprint(st.transfer_cargo(ship,"QUARTZ_SAND",10,drone))
    # st.dock_ship(ship)
    # pprint(st.sell_cargo(ship,"COPPER_ORE",8))
    # pprint(st.get_shipyard(system,"X1-UV97-44217E"))