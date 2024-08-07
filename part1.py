"""Simulates natural selection in the fictional Neebler population."""

import random

# Starting population with each trait variation.
small_neeblers = 300

for neebler in range(small_neeblers):
    # Low chance of being spotted by predators since they're small.
    chance_of_being_spotted = random.randint(0, 4)
    if chance_of_being_spotted == 4:
        small_neeblers = small_neeblers - 1

baby_small_neeblers = 0
for neebler in range(small_neeblers):
    # Smallness trait gets passed to their babies.
    num_babies = random.randint(0, 3)
    baby_small_neeblers = baby_small_neeblers + num_babies

# Babies become the starting population of the next generation.
small_neeblers = baby_small_neeblers

print(str(small_neeblers) + " small Neeblers")
# git marge para fundir os branch