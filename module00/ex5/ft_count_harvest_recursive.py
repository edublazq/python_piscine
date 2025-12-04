#! /usr/bin/env python3

def ft_count_harvest_recursive(n=-1):
    i = -2
    if n == -1:
        n = int(input("Days until harvest: "))
        i = n
    if n > 0:
        ft_count_harvest_recursive(n - 1)
        print(f"Day {n}")
    if i == n:
        print("Harvest Day!")

ft_count_harvest_recursive()
