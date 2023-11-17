print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#Write your code below this line 👇
part_1 = input(
    'You awaken on a damp grassy knoll, there is a long winding path that leads to the "left", and an open field with what looks like a dock to the "right? Where will you go?\n'
).lower()
if part_1 == "left":
    print("You continue your journey")
else:
    (exit(print("You have died! ")))

part_2 = input(
    'Will you try to "swim" the channel or will you "wait" for the boat?\n'
).lower()
if part_2 == "swim":
    (exit(print("You have drowned! ")))
elif part_2 == "wait":
    print(
        "You have waited for the boat to come, you embark on a journey across the sea."
    )
else:
    (exit(
        print(
            "A beast has caught up with you and ripped you to shreds. Game over!"
        )))

part_3 = input(
    'You arrive at a house, and there are three doors present to choose from. One "red", one "blue", and one "yellow". Which will you enter?\n'
).lower()
if part_3 == "red":
    (exit(print("You have been burned alive by fire. Game Over.")))
elif part_3 == "blue":
    (exit(print("You have been ravaged by beasts. Game over")))
elif part_3 == "yellow":
    print("Congratulations, you found the treasure! You Win!")
else:
    (exit(
        print(
            "You have decided to choose nothing. You try to leave and you're killed by the shadows that lurk in the dark. Game over!"
        )))

#sanity

#input('You\'re at a crossroad, where do you want to go? Typpe "left" or "right").lower()
#.lower() at the end can convert the entire input into a lowercase input
#\before a ' negates it
#if choice1 == "left":
#Continue in the game.
#if choice1 == "right: (better option to set the failure as the if and the else as the check point)
#print("You fell into a hole. Game over.")