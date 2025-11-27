def ft_plant_age():
    days_age = int(input("Enter plant age in days: "))
    if days_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
