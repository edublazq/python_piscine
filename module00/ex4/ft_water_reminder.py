def ft_water_remind():
    time_since_last = int(input("Days since last watering: "))
    if time_since_last > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
