from character.entity import Entity


class Monster(Entity):

    def __init__(self, name, health):
        super().__init__(name, health)

    @classmethod
    def create_goblin(cls):
        return cls("Goblin", 100)

    # POLYMORPHIC ATTACK
    def attack(self, target, damage):
        print(f"{self.name} claws {target.name} for {damage} damage")
        target.take_damage(damage)

    def show_status(self):
        print(f"Monster: {self.name}")
        print(f"Health: {self.health}")
        print(f"Alive: {self.is_alive()}")
        print()