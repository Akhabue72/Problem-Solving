class Pet:
    def __init__(self):
        self.name = "Laika"
        self.hunger = 50

    def describe(self):
        print(f"Laika has a hunger of {self.hunger}")

    def feed(self):
        if self.hunger <= 0:
            print(f"{self.name} is already full!")
        else:
            self.hunger -= 5

    def play(self):
        print(f"{self.name} is playing!")
        self.hunger += 10
