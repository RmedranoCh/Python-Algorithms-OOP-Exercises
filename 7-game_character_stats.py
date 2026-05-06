
class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

def character_simulator():
    print("--- HERO CREATOR ---")
    user_name = input("What is your warrior's name?: ")
    character = GameCharacter(user_name)
    
    while True:
        print(f"\n--- {character.name.upper()}'S STATUS ---")
        print(character)
        print("-" * 20)
        print("1. Take Damage")
        print("2. Spend Mana")
        print("3. Level Up (Full Heal)")
        print("4. Exit")
        
        option = input("What do you want to do?: ")

        if option == "1":
            damage = int(input("How much damage do you take?: "))
            character.health -= damage
            print(f"Ouch! Current health: {character.health}")

        elif option == "2":
            cost = int(input("How much mana does the spell cost?: "))
            character.mana -= cost
            print(f"Spell cast. Remaining mana: {character.mana}")

        elif option == "3":
            character.level_up()

        elif option == "4":
            print(f"Goodbye, {character.name}!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    character_simulator()