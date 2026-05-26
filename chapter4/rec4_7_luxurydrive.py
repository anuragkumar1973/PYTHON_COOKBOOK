# rec4_7_luxurydrive.py
from rec4_7_strategy import *
from rec4_7_strategy import StrategyVehicle
from rec4_2 import Vehicle, Car, Truck

car=None  # global to hold the car instance
sporty=None  # global to hold the sporty StrategyVehicle instance

class LuxuryDrive:
    """New strategy implementing a simple luxury driving behavior."""
    def drive(self, vehicle):
        id_ = HelperUtilities._id(vehicle)
        print(f"{id_}: LuxuryDrive: gliding smoothly with premium comfort")
    

def get_existing_sporty():
    try_instantiate = HelperUtilities.try_instantiate
    # create instances (robust to different constructor signatures)
    car = try_instantiate(Car)
    # wrap them with StrategyVehicle and assign initial strategies
    sporty = StrategyVehicle(car, AggressiveDrive())
    return sporty


def demo():
    # Reuse the existing 'sporty' object from rec4_7_strategy.py
    sporty = get_existing_sporty()
    print("\n" + "-" * 40)
    print("Before switching to LuxuryDrive strategy:")
    sporty.drive()
   
    # Set the new strategy (try common setter names)
    try:
        sporty = StrategyVehicle(car, LuxuryDrive())
        sporty.set_strategy(LuxuryDrive())
    except AttributeError:
        sporty._strategy = LuxuryDrive()  # direct assignment as fallback
    
    print("\n" + "-" * 40)
    print("After switching to LuxuryDrive strategy:")
    sporty.drive()

if __name__ == "__main__":
    demo()