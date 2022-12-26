from api import SpaceTraders,TradeSymbol
from pprint import pprint


if __name__ == "__main__":
    st = SpaceTraders()

    jumpWaypoint = "X1-UV97-23539X"
    ship = "FEBATE5T-1"
    drone = "FEBATE5T-2"
    asteroidField ="X1-UV97-24895D"
    contractId="clc3oyf4l000ss60j6lzyx2mv"
    contractIce ="X1-UV97-21170Z"
    copperAlu="X1-UV97-57201E"
    silverGoldPlat="X1-UV97-82653Z"

    
    def cleardrone():
        for c in st.get_my_ship(drone).cargo.inventory:
            if c.symbol != TradeSymbol.ANTIMATTER:
                pprint(st.transfer_cargo(drone,c.symbol,c.units,ship))
    cleardrone()