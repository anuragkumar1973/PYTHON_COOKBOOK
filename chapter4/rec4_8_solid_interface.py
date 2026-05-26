from typing import Protocol, runtime_checkable, Any
from rec4_2 import Vehicle, Car, Truck

"""
re4_8_solid_interface.py

Illustrate SOLID - Interface Segregation Principle by importing and reusing
Vehicle, Car, Truck from rec4_2.py and exposing small, focused interfaces
(Protocols) to clients via lightweight adapters.
"""



@runtime_checkable
class Drivable(Protocol):
    def drive(self, distance: float) -> None:
        ...


@runtime_checkable
class Loadable(Protocol):
    def load(self, weight: float) -> None:
        ...

    def unload(self, weight: float) -> None:
        ...


@runtime_checkable
class Refuelable(Protocol):
    def refuel(self, liters: float) -> None:
        ...


def _call_or_raise(obj: Any, method: str, *args, **kwargs):
    if hasattr(obj, method):
        return getattr(obj, method)(*args, **kwargs)
    raise NotImplementedError(f"{obj!r} does not implement '{method}'")


class CarAdapter(Drivable, Refuelable):
    """Expose only Drivable and Refuelable behavior for a Car instance."""

    def __init__(self, car: Car):
        if not isinstance(car, Vehicle):
            raise TypeError("CarAdapter expects a Vehicle/Car instance")
        self._car = car

    def drive(self, distance: float) -> None:
        _call_or_raise(self._car, "drive", distance)

    def refuel(self, liters: float) -> None:
        _call_or_raise(self._car, "refuel", liters)

    def __repr__(self):
        return f"CarAdapter({self._car!r})"

    def load(self, weight: float) -> False:
        print("\n"+"-"*20+"-ATTENTION-"+"-"*20)
        print("You cannot load cargo with a car, this design is intentional")
        return False

    def unload(self, weight: float) -> False:
        print("\n"+"-"*20+"-ATTENTION-"+"-"*20)
        print("You cannot unload cargo with a car, this design is intentional")
        return False

class TruckAdapter(Drivable, Loadable, Refuelable):
    """Expose Drivable, Loadable and Refuelable behavior for a Truck instance."""

    def __init__(self, truck: Truck):
        if not isinstance(truck, Vehicle):
            raise TypeError("TruckAdapter expects a Vehicle/Truck instance")
        self._truck = truck

    def drive(self, distance: float) -> None:
        _call_or_raise(self._truck, "drive", distance)

    def load(self, weight: float) -> None:
        _call_or_raise(self._truck, "load", weight)

    def unload(self, weight: float) -> None:
        _call_or_raise(self._truck, "unload", weight)

    def refuel(self, liters: float) -> None:
        _call_or_raise(self._truck, "refuel", liters)

    def __repr__(self):
        return f"TruckAdapter({self._truck!r})"


# Client functions depend only on the small interfaces they need:
def perform_trip(vehicle: Drivable, distance: float) -> None:
    vehicle.drive(distance)


def refuel_vehicle(r: Refuelable, liters: float) -> None:
    r.refuel(liters)


def load_cargo(loader: Loadable, weight: float) -> None:
    loader.load(weight)


if __name__ == "__main__":
    # Instantiate domain objects provided in rec4_2.py
    sedan = Car("Toyota", "Corolla", 2018, mileage=14000)    # reuses Car from rec4_2.py
    hauler = Truck("Ford", "F-150", 2017, mileage=7500, max_load_kg=3000)  # reuses Truck from rec4_2.py


    # Wrap them with adapters that present only the required interfaces
    car = CarAdapter(sedan)
    truck = TruckAdapter(hauler)

    # Clients use small interfaces: they don't need to know about other methods
    perform_trip(car, 120.5)
    perform_trip(truck, 55.0)

    #refuel_vehicle(car, 40.0)
    #refuel_vehicle(truck, 150.0)

    print("\n"+"-"*20+"-TRYIN TO LOAD TRUCK-"+"-"*20)
    print("Truck info before loading:", truck)
    load_cargo(truck, 500.0)
    print("Truck info after loading:", isinstance(truck, Loadable))

    # Demonstrate interface segregation: car is not Loadable
    try:
        print("\n"+"-"*20+"-TRYIN TO LOAD CAR-"+"-"*20)
        load_cargo(car, 100.0)  # will raise NotImplementedError
    except NotImplementedError as e:
        print("\n"+"-"*20+"-ATTENTION-"+"-"*20)
        print("You cannot load cargo with a car, this design is intentional")