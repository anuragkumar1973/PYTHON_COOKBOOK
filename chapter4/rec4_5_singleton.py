from rec4_2 import Vehicle
from rec4_2 import Car, Truck

"""
rec4_5_singleton.py

Illustrate the Singleton pattern for the Vehicle class defined in rec4_2.py.

This file defines a Singleton metaclass and then subclasses Vehicle to create a
singleton Vehicle type. The demonstration shows that multiple "instantiations"
return the same object.
"""



class SingletonMeta(type):
    """Metaclass that ensures only one instance per class."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in SingletonMeta._instances:
            SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)
        return SingletonMeta._instances[cls]


class SingletonVehicle(Vehicle, metaclass=SingletonMeta):
    """A Vehicle subclass that is a singleton."""
    pass


if __name__ == "__main__":
    # Try calling with some example init args; if Vehicle signature differs,
    # fall back to no-arg construction.
    try:
        car = Vehicle("GMC", "Acadia", year=2026)
        truck = Vehicle("Ford", "F-150", year=2024)
        v1 = SingletonVehicle(car.make, car.model, car.year)
        v2 = SingletonVehicle(truck.make, truck.model, truck.year)
    except TypeError:
        v1 = SingletonVehicle()
        v2 = SingletonVehicle()

    print("v1 is v2:", v1 is v2)
    print("v1 id:", id(v1))
    print("v2 id:", id(v2))
    
    print("\n","-"*50 )
    print("v1 info:", v1.info())
    print("v2 info:", v2.info())    

    # Show that attributes are shared (demonstration depends on Vehicle implementation)
    try:
        print("\nv1 state:---", v1.__dict__)
        print("v2 state:---", v2.__dict__)
        print("\nCar's infor:--", car.info())
        print("Truck's info:--", truck.info())
    except Exception:
        # If Vehicle uses __slots__ or custom repr, just show repr
        print("v1 repr:", repr(v1))
        print("v2 repr:", repr(v2))
    print("\n","-"*50 )
  