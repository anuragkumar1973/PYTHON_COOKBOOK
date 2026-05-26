from rec4_2 import Vehicle, Car, Truck
import inspect

# HelperUtilities class to host previously module-level helper functions
class HelperUtilities:
    @staticmethod
    def _id(vehicle):
        # try to return a sensible identifier for the vehicle
        for attr in ("name", "model", "make"):
            val = getattr(vehicle, attr, None)
            if val:
                return f"{vehicle.__class__.__name__}({val})"
        return vehicle.__class__.__name__

    @staticmethod
    def try_instantiate(cls):
        """
        Try several common constructor signatures to create an instance.
        Falls back to creating a plain Vehicle or a minimal dummy object.
        """
        attempts = [
            (),                         # no-arg
            ("Demo",),                  # single name
            ("DemoMake", "DemoModel"),  # make, model
            ("DemoMake", "DemoModel", 2020),  # make, model, year
        ]
        for args in attempts:
            try:
                return cls(*args)
            except TypeError:
                continue
        # Try to instantiate as Vehicle if cls is not Vehicle
        if cls is not Vehicle:
            try:
                return Vehicle()
            except Exception:
                pass
        # final fallback: simple dummy object with a class-like string
        class Dummy:
            pass
        return Dummy()


# Strategy implementations
class AggressiveDrive:
    def drive(self, vehicle):
        id_ = HelperUtilities._id(vehicle)
        print(f"{id_}: driving aggressively — high RPM, rapid acceleration")

class DefensiveDrive:
    def drive(self, vehicle):
        id_ = HelperUtilities._id(vehicle)
        print(f"{id_}: driving defensively — smooth braking, large following distance")

class EcoDrive:
    def drive(self, vehicle):
        id_ = HelperUtilities._id(vehicle)
        print(f"{id_}: driving economically — low RPM, gentle acceleration")

# Wrapper that applies a drive strategy to any vehicle instance
class StrategyVehicle:
    def __init__(self, vehicle, strategy):
        self._vehicle = vehicle
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def drive(self):
        # delegate driving to the current strategy
        self._strategy.drive(self._vehicle)

    # delegate attribute access to the wrapped vehicle
    def __getattr__(self, name):
        return getattr(self._vehicle, name)


def demo():
    # module-level aliases to preserve the original API used elsewhere in the file
    _id = HelperUtilities._id
    try_instantiate = HelperUtilities.try_instantiate
    # rec4_7_strategy.py
    # Demonstrate Strategy pattern using Vehicle, Car and Truck from rec4_2.py
    
    # create instances (robust to different constructor signatures)
    car = try_instantiate(Car)
    truck = try_instantiate(Truck)

    # wrap them with StrategyVehicle and assign initial strategies
    sporty = StrategyVehicle(car, AggressiveDrive())
    haul = StrategyVehicle(truck, DefensiveDrive())
    print("\n" + "-" * 40)
    print("Initial behavior:")
    sporty.drive()
    haul.drive()

    print("\n" + "-" * 40)
    print("\nSwitching strategies at runtime:")
    sporty.set_strategy(EcoDrive())   # change car to eco mode
    haul.set_strategy(AggressiveDrive())  # make truck aggressive for a moment

    sporty.drive()
    haul.drive()

    print("\n" + "-" * 40)
    print("\nMixing strategies and direct vehicle attributes (delegation):")
    # show that other attributes/methods of the underlying vehicle are still accessible
    # prints class name and any known attributes
    for sv in (sporty, haul):
        print(f"- Wrapped object type: {sv._vehicle.__class__.__name__}")
        # try to call a 'start' or 'stop' method if present (common in vehicle examples)
        for method in ("start", "stop"):
            if hasattr(sv, method) and inspect.isroutine(getattr(sv, method)):
                print(f"  Calling {method}() on {sv._vehicle.__class__.__name__}")
                getattr(sv, method)()

if __name__ == "__main__":
    demo()
    print("\n" + "-" * 40)