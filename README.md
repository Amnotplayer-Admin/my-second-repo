# Simple Battle Simulator

This Python battle simulation pits a heroic Knight against two enemies, a Goblin and an Orc. It demonstrates object-oriented programming with character classes and a turn-based battle.

## File Structure

- `character.py`: Defines the `Character` class and its combat behavior.
- `main.py`: Runs a battle between the Knight and both enemies.

## Character Class

Located in `character.py`, the `Character` class includes:

### Attributes
- `name` (str): The character's name.
- `hp` (number): Current hit points.
- `attack_power` (number): The attack's initial power. Each attack deals a random 30%-90% of this value.

### Methods
- `attack(other)`: Randomly reduces the other character's HP by 30%-90% of the attacker's initial attack power, without reducing HP below zero.
- `is_alive()`: Returns `True` if HP is greater than 0.
- `__str__()`: Returns a string representation of the character's current HP.

## How the Battle Works

1. Create a Knight, a Goblin, and an Orc.
2. Print their initial stats.
3. The Knight attacks each living enemy, then each surviving enemy attacks the Knight.
4. Repeat until the Knight or both enemies are defeated, then declare the result.

## Running the Game

Execute `main.py`:

```bash
python main.py
```
