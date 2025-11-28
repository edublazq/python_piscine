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

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
    
    @property
    def trunk_diameter(self):
        return self.__trunk_diameter
    
    @trunk_diameter.setter
    def trunk_diameter(self, nb):
        if nb > 0:
            self.__trunk_diameter = nb
        else:
            print("Invalid Trunk diameter!! [REJECTED]")

    def produce_shade(self):
        area = (3.141592 * self.trunk_diameter/2 *self.trunk_diameter / 2) / 100
        print(f"{self.name} provides {area:.2f} square meters of shade")
    
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old, trunk_diameter = {self.__trunk_diameter}")

class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beatifully!")

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old, color = {self.color}")

class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old, {self.harvest_season}, {self.nutritional_value}")

if __name__ == "__main__":
    trees = []
    flowers = []
    vegetables = []
    i = 1

    while i <= 2:
        new_tree = Tree(f"tree_{i}", i * 30, i * 100, i * 10)
        new_flower = Flower(f"flower_{i}", i * 3, i * 5, "red")
        new_vegetable = Vegetable(f"vegetable_{i}", i * 2, i * 30, "spring", "Vitamin A")
        trees.append(new_tree)
        flowers.append(new_flower)
        vegetables.append(new_vegetable)
        i += 1
    trees[0].get_info()
    trees[1].get_info()
    flowers[0].get_info()
    flowers[1].get_info()
    vegetables[0].get_info()
    vegetables[1].get_info()
