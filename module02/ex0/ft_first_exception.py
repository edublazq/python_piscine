#! /usr/bin/env python3

def test_temperature_input():
    temp_str = input("\nTesting temperature: ")
    try:
        int(temp_str)
    except:
        print(f"{temp_str} is not a number")
        return
    return temp_str

def check_temperature(temp_str):

    if temp_str == None:
        return
    else:
        temp = int(temp_str)
    if temp <= 40 and temp >= 0:
        print(f"Temperature {temp_str}ºC is perfect for this plants!")
    elif temp > 40:
        print(f"Temperature {temp_str}ºC is too high! (Max 40º)")
    elif temp < 0:
        print(f"Temperature {temp_str}ºC is too low! (Min 0º)")


if __name__ == "__main__":
    print("==========GARDEN TEMPERATURE CHECK==========")
    for i in range(0, 4):
        check_temperature(test_temperature_input())
