#! /usr/bin/env python3

def garden_operations(exec: int):
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    match exec:
        case 0:
            int("abc")
        case 1:
            n = 4 / 0
            print(f"{n}")
        case 2:
            open("imposiblequeexista.txt", "r")
        case 3:
            thisdict.get("horse")
        case 4:
            for i in range(0, 4):
                garden_operations(i)


def test_error_types():
    for i in range(0, 4):
        try:
            garden_operations(i)
        except ValueError as error_msg:
            print(f"Caught value error: {error_msg}")
        except ZeroDivisionError as error_msg:
            print(f"Caught zero division error: {error_msg}")
        except FileNotFoundError as error_msg:
            print(f"Caught file not found error: {error_msg}")
    try:
        garden_operations(4)
    except Exception:
        print("Caught an error! (program is still on running)")


if __name__ == "__main__":
    test_error_types()
