def ft_harvest_total():
    harvest_total = 0
    i = 1
    while i < 4:
        harvest_total += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest {harvest_total}")
