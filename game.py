# program name   :   snake water gun game
# author         :   Dev Yash
# date           :   04/july/2021

import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

    


print("computer turn Turn: snake(s) water(w) or gun(g)?\n")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

print(".................................................")
you = input("your Turn: snake(s) water(w) or gun(g)?         |\n")
print("                                                |")
print(".................................................")
a = game(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("......................")
    print("the game is tie      |")
    print("......................")
elif a:
    print("......................")
    print("you won the game     |")
    print("......................")
else:
    print("......................")
    print("you loose            |")
    print("......................")
