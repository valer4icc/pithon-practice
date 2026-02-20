from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, target, damage):
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    @abstractmethod
    def show_status(self):
        pass