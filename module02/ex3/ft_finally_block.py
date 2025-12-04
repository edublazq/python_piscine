#! /usr/bin/env python3

def water_plants(plant_list):
    print("====== OPEN WATERING SYSTEM ======")
    for plant in plant_list:
        try:
            if plant is None:
                raise Exception("Not legible name")
            print(f"Watered {plant} xd")
        except Exception as err_msg:
            print(f"{err_msg}")
        finally:
            print("\nFunction still running!!!!\n")


def test_watering_system():
    list = [None, "tomatoes", "lettuce", None, "carrots"]
    water_plants(list)

if __name__ == "__main__":
    test_watering_system()
