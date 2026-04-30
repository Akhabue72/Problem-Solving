class player:
    def __init__(self):
        self.name = "Ollie"
        self.health = 75
        self.attack = 110
        self.defence = 74
        self.sptk = 110
        self.spdf = 66
        self.speed = 140

    def describe(self):
        print(f"Character: <{self.name}> | Health: {self.health}/100 | Attack: <{self.attack}> | Defence: <{self.defence}>")

    def Heal(self):
        if self.health >= 100:
            print(f"{self.name} is already full health!")
        else:
            self.health += 5

    def takeDamage(self):
        print(f"{self.name} has taken damage!")
        self.health -= 10


# print("=" * 50)
# print("BREAD PATCHNOTES")
# print("=" * 50)
# print("""
# Ollie Balance changes:
#
# - Hp:100 -> 120
# - Atk:5 -> 110
# - Def:95 -> 74
# - sptk:150 -> 110
# - spdf:100 -> 66
# - spd:150 -> 140
# - Ability: Slow start -> Convergence""")