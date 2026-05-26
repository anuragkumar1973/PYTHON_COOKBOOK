from abc import ABC, abstractmethod
from typing import List

# /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter4/rec4_1.py


class Vehicle(ABC):
    """Abstract base for all vehicles."""
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @property
    def name(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    @abstractmethod
    def move(self) -> str:
        """Describe how the vehicle moves."""
        pass

    def describe(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"


# Simple categories
class TwoWheeler(Vehicle):
    wheels = 2

    def move(self) -> str:
        return f"{self.describe()} is ridden on {self.wheels} wheels."


class FourWheeler(Vehicle):
    wheels = 4

    def move(self) -> str:
        return f"{self.describe()} is driven on {self.wheels} wheels."


# Mixins to add capabilities and demonstrate multiple inheritance behavior
class ElectricMixin:
    def __init__(self, battery_kwh: float = 0.0, *args, **kwargs):
        # allow cooperative multiple inheritance initialization
        super().__init__(*args, **kwargs)
        self.battery_kwh = battery_kwh

    def charge(self, kwh: float) -> None:
        self.battery_kwh += kwh

    def move(self) -> str:
        # cooperative method: enhance behavior then call next in MRO
        base = super().move()
        return f"(electric {self.battery_kwh}kWh) {base}"


class CombustionMixin:
    def __init__(self, fuel_liters: float = 0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_liters = fuel_liters

    def refuel(self, liters: float) -> None:
        self.fuel_liters += liters

    def move(self) -> str:
        base = super().move()
        return f"(combustion {self.fuel_liters:.1f}L) {base}"


class OffroadMixin:
    def __init__(self, ground_clearance_cm: float = 20.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ground_clearance_cm = ground_clearance_cm

    def engage_4wd(self) -> str:
        return f"{self.describe()} engaged 4WD (clearance {self.ground_clearance_cm} cm)."


class CargoMixin:
    def __init__(self, cargo_capacity_kg: float = 0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cargo_capacity_kg = cargo_capacity_kg

    def load_cargo(self, kg: float) -> str:
        if kg > self.cargo_capacity_kg:
            return f"Over capacity! {kg}kg > {self.cargo_capacity_kg}kg"
        return f"Loaded {kg}kg into {self.describe()} (capacity {self.cargo_capacity_kg}kg)."


# Concrete vehicles showing multiple inheritance combinations
class Bicycle(TwoWheeler):
    def __init__(self, make: str, model: str, year: int):
        super().__init__(make, model, year)

    def pedal(self) -> str:
        return f"{self.describe()} is being pedaled."


class Motorcycle(CombustionMixin, TwoWheeler):
    def __init__(self, make: str, model: str, year: int, fuel_liters: float = 5.0):
        super().__init__(fuel_liters=fuel_liters, make=make, model=model, year=year)

    def wheelie(self) -> str:
        return f"{self.describe()} pops a wheelie!"


class Scooter(ElectricMixin, TwoWheeler):
    def __init__(self, make: str, model: str, year: int, battery_kwh: float = 1.5):
        super().__init__(battery_kwh=battery_kwh, make=make, model=model, year=year)


class Car(CombustionMixin, FourWheeler):
    def __init__(self, make: str, model: str, year: int, fuel_liters: float = 40.0):
        super().__init__(fuel_liters=fuel_liters, make=make, model=model, year=year)


class ElectricCar(ElectricMixin, FourWheeler):
    def __init__(self, make: str, model: str, year: int, battery_kwh: float = 75.0):
        super().__init__(battery_kwh=battery_kwh, make=make, model=model, year=year)


class Pickup(CombustionMixin, CargoMixin, FourWheeler):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        fuel_liters: float = 80.0,
        cargo_capacity_kg: float = 1000.0,
    ):
        super().__init__(fuel_liters=fuel_liters, cargo_capacity_kg=cargo_capacity_kg, make=make, model=model, year=year)


class ElectricSUV(ElectricMixin, OffroadMixin, FourWheeler):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        battery_kwh: float = 100.0,
        ground_clearance_cm: float = 25.0,
    ):
        super().__init__(battery_kwh=battery_kwh, ground_clearance_cm=ground_clearance_cm, make=make, model=model, year=year)


def demo(vehicles: List[Vehicle]) -> None:
    for v in vehicles:
        print("-" * 60)
        print(v.describe())
        print("move():", v.move())
        # mixin-specific capabilities tested dynamically
        if isinstance(v, ElectricMixin):
            print(" - is electric:", getattr(v, "battery_kwh", None), "kWh")
            v.charge(5.0)
            print(" - after charging:", v.battery_kwh, "kWh")
        if isinstance(v, CombustionMixin):
            print(" - fuel:", getattr(v, "fuel_liters", None), "L")
            v.refuel(10.0)
            print(" - after refuel:", v.fuel_liters, "L")
        if isinstance(v, CargoMixin):
            print(" - cargo test:", v.load_cargo(200.0))
        if isinstance(v, OffroadMixin):
            print(" - offroad:", v.engage_4wd())

    # show MRO for a class that uses multiple inheritance
    print("\nMethod Resolution Order for ElectricSUV:")
    for cls in ElectricSUV.__mro__:
        print(" ", cls.__name__)


if __name__ == "__main__":
    fleet: List[Vehicle] = [
        Bicycle("Giant", "Escape 3", 2022),
        Motorcycle("Yamaha", "MT-07", 2021, fuel_liters=14.0),
        Scooter("Xiaomi", "M365", 2020, battery_kwh=0.5),
        Car("Toyota", "Corolla", 2019, fuel_liters=50.0),
        ElectricCar("Tesla", "Model 3", 2022, battery_kwh=82.0),
        Pickup("Ford", "F-150", 2020, fuel_liters=65.0, cargo_capacity_kg=1400.0),
        ElectricSUV("Rivian", "R1S", 2023, battery_kwh=135.0, ground_clearance_cm=30.0),
    ]

    demo(fleet)