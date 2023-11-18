names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
indexNum = random.randint(0, len(names))
randName = names[indexNum]
print(f"{randName} is going to buy the meal today!")