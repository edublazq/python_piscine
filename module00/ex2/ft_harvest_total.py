def ft_harvest_total():
    harvest_total = 0
    for i in range(1, 4):
        harvest_total += int(input(f"Day {i} harvest: "))
    print(f"Total harvest {harvest_total}")
