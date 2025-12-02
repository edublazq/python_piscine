#! /usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height, days):
        self.__name = name
        self.__height = height
        self.__age = days
        print(f"Plant {self.name} created.")
        print(f"({self.height}cm, {self.age} days old)")

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

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.__age} days old")


if __name__ == "__main__":
    plant = SecurePlant("Marcelo", 15, 20)
    plant.age = 12
    plant.get_info()
    plant.age = -1
    plant.get_info()
