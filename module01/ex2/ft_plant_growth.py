#! /usr/bin/env python3

class plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self):
        self.height += 1

    def age(self):
        self.age_days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    i = 1
    plant_1 = plant("Rosa", 10, 30)
    plant_2 = plant("Sunflower", 25, 12)
    plant_3 = plant("Cactus", 100, 300)
    while i <= 7:
        print(f"Day {i}")
        plant_1.get_info()
        plant_2.get_info()
        plant_3.get_info()
        print("________________________")
        plant_1.age()
        plant_2.age()
        plant_3.age()
        if i % 2 == 0:
            plant_1.grow()
            plant_3.grow()
        else:
            plant_2.grow()
        i += 1
