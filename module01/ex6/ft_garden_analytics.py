#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.__name = name
        self.__height = height
        self.__age = days
        print(f"Plant {self.__name} created. ({self.__height}cm, {self.__age} days old)")

    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @property
    def age(self):
        return self.__age

    @height.setter
    def height(self, nb):
        if nb < 0:
            print("Invalid height assignation [REJECTED]")
        else:
            self.__height = nb

    @age.setter
    def age(self, nb):
        if nb < 0:
            print("Invalid age assignation [REJECTED]")
        else:
            self.__age = nb

    @name.setter
    def name(self, str):
        self.__name = str

    def add_age(self):
        self.age += 1

    def add_cm(self):
        self.height += 1

class Flowering_Plant(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beatifully {self.color} petals!")

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old, color = {self.color}")

class PrizeFlower(Flowering_Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)

    def looking(self):
        print(f"You stopped to look at {self.name}")

class Garden:
    def __init__(self, first_plant):
        self.__plants = []
        if not isinstance(first_plant, Plant):
            print (f"{first_plant} is not a plant, object wasn't created")
            return
        else:
            self.__plants.append(first_plant)

    @property
    def plants(self):
        return self.__plants

    @plants.setter
    def plants(self, *new_plants):
        self.__plants.clear()
        for plant in new_plants:
            if not isinstance(plant, Plant):
                print (f"{plant} is not a plant [REJECTED]")
                return
            else:
                self.__plants.append(plant)

    def add_plants(self, *new_plants):
        for plant in new_plants:
            if not isinstance(plant, Plant):
                print (f"{plant} is not a plant [REJECTED]")
                return
            else:
                self.__plants.append(plant)

class GardenManager:
    def __init__(self, *gardens):
        self.__gardens = []
        for garden in gardens:
            if isinstance(garden, Garden):
                self.__gardens.append(garden)
            else:
                print(f"{garden} is not a garden [REJECTED]")
    
    @classmethod
    def create_garden_network(cls, *gardens):
        return cls(gardens)

    @property
    def gardens(self):
        return self.__gardens

    @gardens.setter
    def gardens(self, *gardens):
        for garden in gardens:
            if isinstance(garden, Garden):
                self.__gardens.append(garden)
            else:
                print(f"{garden} is not a garden [REJECTED]")

    def GardenStats(self):
        print("________________")
        print("GARDEN REPORT")
        print("________________")
        plants = 0
        i = []
        normal_plants = 0
        flowering_plants = 0
        prize_flowers = 0
        for garden in self.gardens:
            for plant in garden.plant:
                plants += 1
                if isinstance(plant, Plant):
                    if isinstance(plant, Flowering_Plant):
                        if isinstance(plant, PrizeFlower):
                            i.append(2)
                        else:
                            i.append(1)
                    else:
                        i.append(0)
        for j in i:
            if j == 2:
                prize_flowers += 1
            if j == 1:
                flowering_plants += 1
            if j == 0:
                normal_plants += 1
        print(f"You have {plants} plants")
        print(f" {normal_plants} Standard Plants")
        print(f" {flowering_plants} Flowering Plants")
        print(f" {prize_flowers} Prize Flowers")
