import random

dice_rolled = random.randint(1,6)

if dice_rolled == 1 or dice_rolled == 6:
    print(f"Wylosowano {dice_rolled}", True)
else:
    print(f"Wylosowano {dice_rolled}", False)