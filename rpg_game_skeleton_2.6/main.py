from character.character import Character
from character.monster import Monster
from combat.combat import perform_attack


def main():
    hero = Character("Petras")
    goblin = Monster.create_goblin()

    perform_attack(hero, goblin, 30)
    perform_attack(goblin, hero, 15)

    hero.show_status()
    goblin.show_status()


if __name__ == "__main__":
    main()