#! /usr/bin/env python3


class Plant:
    def __init__(self, name, height, days):
        self.__name = name
        self.__height = height
        self.__age = days
        print(
            f"Plant {self.__name} created. ({self.__height}cm, {self.__age} days old)"
        )

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


class FloweringPlant(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beatifully {self.color} petals!")

    def get_info(self):
        print(
            f"{self.name}: {self.height}cm, {self.age} days old, color = {self.color}"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.__prize_points = prize_points

    @property
    def prize_points(self):
        return self.__prize_points

    @prize_points.setter
    def prize_points(self, nb):
        if isinstance(nb, int):
            self.__prize_points = nb
        else:
            print(f"{nb} is not an integer [REJECTED]")

    def looking(self):
        print(f"You stopped to look at {self.name}")


class Garden:
    def __init__(self, name, *plants):
        self.__plants = []
        self.__name = name
        for plant in plants:
            # if isinstance(plant, Plant):
            #     self.__plants.append(plant)
            # elif isinstance(plant, PrizeFlower):
            #     self.__plants.append(plant)
            # elif isinstance(plant, FloweringPlant):
            self.__plants.append(plant)
            # else:
            #     print (f"{plant} is not a plant of any type")
            # return
        print(f"Plants: {self.__plants}")

    @property
    def plants(self):
        return self.__plants

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print(f"{new_name} is not a string [REJECTED]")

    @plants.setter
    def plants(self, *new_plants):
        self.__plants.clear()
        for plant in new_plants:
            if not isinstance(plant, Plant):
                print(f"{plant} is not a plant [REJECTED]")
                return
            else:
                self.__plants.append(plant)

    def add_plants(self, *new_plants):
        for plant in new_plants:
            if not isinstance(plant, Plant):
                print(f"{plant} is not a plant [REJECTED]")
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
        normal_plants = 0
        flowering_plants = 0
        prize_flowers = 0
        for garden in self.gardens:
            print("===========================")
            print(f"GARDEN: {garden.name}")
            print("===========================")
            for plant in garden.plants:
                print(f"{plant.name}:")
                print(f"Statistics: {plant.height}cm {plant.age} days")
                if isinstance(plant, FloweringPlant):
                    print(f"Color: {plant.color}")
                    if isinstance(plant, PrizeFlower):
                        print(f"Prize points: {plant.prize_points}")
                        prize_flowers += 1
                    else:
                        flowering_plants += 1
                else:
                    normal_plants += 1
                print("_________________________________")
        plants = normal_plants + prize_flowers + flowering_plants
        print(f"You have {plants} plants")
        print(f" {normal_plants} Standard Plants")
        print(f" {flowering_plants} Flowering Plants")
        print(f" {prize_flowers} Prize Flowers")


if __name__ == "__main__":
    plants_garden1 = []
    for i in range(1, 4):
        new_flower = FloweringPlant(f"Plant_{i}", 30, 12, "Red")
        plants_garden1.append(new_flower)
        print(f"{plants_garden1[i - 1].name} added")
    garden_1 = Garden("My_garden", *plants_garden1)
    garden_manager = GardenManager(garden_1)
    garden_manager.GardenStats()
