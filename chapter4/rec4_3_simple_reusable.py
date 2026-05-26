from typing import List

#!/usr/bin/env python3
"""
rec4_3.py

Demonstrates object-oriented reusability with a base Vehicle class reused via
object instance creation.
"""

class Vehicle:
    """
    Reusable base class for vehicles.
    """
    MAINTENANCE_INTERVAL_KM = 10000  # default interval for maintenance

    def __init__(self, make: str, model: str, year: int, mileage: int = 0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = int(mileage)
        self.engine_on = False

    def start(self):
        self.engine_on = True
        return f"{self.make} {self.model}: engine started."

    def stop(self):
        self.engine_on = False
        return f"{self.make} {self.model}: engine stopped."

    def drive(self, km: int):
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.mileage += int(km)
        return f"{self.make} {self.model}: drove {km} km (total {self.mileage} km)."

    def needs_maintenance(self) -> bool:
        return self.mileage >= self.MAINTENANCE_INTERVAL_KM

    def info(self) -> str:
        return f"{self.year} {self.make} {self.model} — mileage: {self.mileage} km"


def demo():
    # Create vehicles (reusing Vehicle via subclasses)
    
    v1=Vehicle("Generic", "E-Bike", 2020, mileage=500)
    v2=Vehicle("Generic", "Bike", 2020, mileage=500)
    
    print("\n","-"*40)
    print(v1.start())
    print(v1.info())
    print(v1.drive(15000))

    print("\n","-"*40)
    print(v2.start())
    print(v2.drive(200))
    print(v2.info())

    print("\n","-"*40)
    if v1.needs_maintenance():
        print(f"{v1.make} {v1.model} needs maintenance.")
    else:
        print(f"{v1.make} {v1.model} does not need maintenance yet.")

if __name__ == "__main__":
    demo()