from typing import List

#!/usr/bin/env python3
"""
rec4_2.py

Demonstrates object-oriented reusability with a base Vehicle class reused via
inheritance (Car, Truck) and composition (Fleet).
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


class Car(Vehicle):
    """
    Car reuses Vehicle behavior; change maintenance threshold for cars.
    """
    MAINTENANCE_INTERVAL_KM = 15000  # cars might have longer intervals

    def open_trunk(self):
        return f"{self.make} {self.model}: trunk opened."


class Truck(Vehicle):
    """
    Truck reuses Vehicle and adds load-handling behavior.
    """
    MAINTENANCE_INTERVAL_KM = 8000  # heavier usage may need earlier maintenance

    def __init__(self, make: str, model: str, year: int, mileage: int = 0, max_load_kg: int = 5000):
        super().__init__(make, model, year, mileage)
        self.max_load_kg = int(max_load_kg)
        self.current_load_kg = 0

    def load(self, kg: int):
        potential = self.current_load_kg + int(kg)
        if potential > self.max_load_kg:
            raise ValueError("Exceeds truck max load")
        self.current_load_kg = potential
        return f"{self.make} {self.model}: loaded {kg} kg (current {self.current_load_kg} kg)."

    def unload(self, kg: int):
        removed = min(self.current_load_kg, int(kg))
        self.current_load_kg -= removed
        return f"{self.make} {self.model}: unloaded {removed} kg (current {self.current_load_kg} kg)."

    def info(self) -> str:
        base = super().info()
        return f"{base} — load: {self.current_load_kg}/{self.max_load_kg} kg"


class Fleet:
    """
    Composition example: Fleet manages many Vehicle instances, reusing the Vehicle API.
    """
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, v: Vehicle):
        self.vehicles.append(v)

    def total_mileage(self) -> int:
        return sum(v.mileage for v in self.vehicles)

    def vehicles_needing_maintenance(self) -> List[Vehicle]:
        return [v for v in self.vehicles if v.needs_maintenance()]

    def find(self, *, make: str = None, model: str = None) -> List[Vehicle]:
        results = self.vehicles
        if make:
            results = [v for v in results if v.make.lower() == make.lower()]
        if model:
            results = [v for v in results if v.model.lower() == model.lower()]
        return results


def demo():
    # Create vehicles (reusing Vehicle via subclasses)
    v1=Vehicle("Generic", "E-Bike", 2020, mileage=500)
    v2=Vehicle("Generic", "Bike", 2020, mileage=500)
    v3=Car("Toyota", "Corolla", 2018, mileage=14000)
    v4=Truck("Ford", "F-150", 2017, mileage=7500, max_load_kg=3000)
    
    print(v1.start())
    print(v1.drive(1500))
    
    print(v2.start)
    print(v2.drive(200))

    print(v3.start())
    print(v3.drive(600))       # pushes car over its maintenance threshold
    print(v3.stop())
    print(v3.open_trunk())
   
    print(v4.load(1200))
    print(v4.drive(1000))
    print(v4.unload(200))

if __name__ == "__main__":
    demo()