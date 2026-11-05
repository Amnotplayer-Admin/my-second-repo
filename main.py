from character import Character


def main():
    hero = Character("Knight", 30, 5)
    enemies = [
        Character("Goblin", 20, 3),
        Character("Orc", 20, 3),
    ]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(enemy.is_alive() for enemy in enemies):
        for enemy in enemies:
            if enemy.is_alive():
                hero.attack(enemy)

        for enemy in enemies:
            if enemy.is_alive():
                enemy.attack(hero)
                if not hero.is_alive():
                    break

        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()
