from character.entity import Entity


class Character(Entity):

    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self, target, damage):
        print(f"{self.name} strikes {target.name} for {damage} damage")
        target.take_damage(damage)

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Alive: {self.is_alive()}")
        print()