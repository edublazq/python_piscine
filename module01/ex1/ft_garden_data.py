#! /usr/bin/env python3

class plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def get_info(self):
		print("____________________________")
		print(f"Plant name: {self.name}")
		print(f"Plant height: {self.height} cm")
		print(f"Plant age: {self.age} days")
		print("____________________________")

if __name__ == "__main__":
	plant_1 = plant("Rosa", 10, 30)
	plant_2 = plant("Sunflower", 25, 12)
	plant_3 = plant("Cactus", 100, 300)
	plant_1.get_info()
	plant_2.get_info()
	plant_3.get_info()
