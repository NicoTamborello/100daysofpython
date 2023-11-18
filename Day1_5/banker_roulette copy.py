names = ["Jenny", "Todd"]

import random

num_items = len(names)
random_choice = random.randint(0, num_items -1)

print(f"{names[random_choice]} is going to buy the meal today!")