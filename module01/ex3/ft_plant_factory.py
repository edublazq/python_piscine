#! /usr/bin/env python3

class plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days
        print(f"Plant {self.name} created.")
        print(f"({self.height}cm, {self.age_days} days old)")

    def grow(self):
        self.height += 1

    def age(self):
        self.age_days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    plants = []
    i = 0
    while i < 5:
        new_plant = plant(f"Plant_{i+1}", 10 * (i + 1), 5 * (i + 1))
        plants.append(new_plant)
        i += 1
    print(f"Plants created: {i}")
