from abc import ABC, abstractmethod


## abstract class
class Enforce(ABC):
    @abstractmethod
    def start_engine():
        pass


class Bike(Enforce):
    pass


class Car(Enforce):
    pass


class Truck(Enforce):
    pass
