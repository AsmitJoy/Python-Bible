import random

health = 100

difficulty = 1

posion_health = int(random.randint(25,50) / difficulty)

health = health + posion_health

print(health)
