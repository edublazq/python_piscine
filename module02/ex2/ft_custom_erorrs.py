#! /usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)


def error_checker(error: int):
    match(error):
        case 0:
            raise PlantError("The tomato plant is wilting")
        case 1:
            raise WaterError("Not enough water in the tank")
        case 2:
            raise GardenError("The tomato plant is wilting")
        case 3:
            raise GardenError("Not enough water in the tank")

if __name__ == "__main__":
    print("=== CUSTOM GARDEN ERRORS ===")
    for i in range(0, 4):
        print(f"\nTesting {i} error")
        try:
            error_checker(i)
        except GardenError as error_msg:
            print(f"Caught {type(error_msg).__name__}: {error_msg}")
    print("\nProgram ended without stopping on errors!")

