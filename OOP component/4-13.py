from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, speed):
        self._speed = speed

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self._speed = 0

    @property
    @abstractmethod
    def speed(self):
        """기체의 속도를 설정하는 getter method"""
        pass


print(Vehicle.mro())
print(dir(Vehicle))
