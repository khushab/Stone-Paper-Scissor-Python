import random
import time


def game(randno, you):
    if randno == you:
        return None

    if randno == 1:
        if you == 2:
            return True
        elif you == 3:
            return False

    if randno == 2:
        if you == 1:
            return False
        elif you == 3:
            return True

    if randno == 3:
        if you == 1:
            return True
        elif you == 2:
            return False


print("Computer's Turn: Rock(1), Paper(2), Sissor(3)\n")

randno = random.randint(1, 3)

if randno == 1:
    comp = 'Rock'
elif randno == 2:
    comp = 'Paper'
else:
    comp = 'Sissor'
time.sleep(1)

you = int(input("Your Turn: Rock(1), Paper(2), Sissor(3)\n"))

if you == 1:
    pchoice = 'Rock'
elif you == 2:
    pchoice = 'Paper'
elif you == 3:
    pchoice = 'Sissor'
else:
    print("Invalid!")


output = game(randno, you)

print(f"Computer Choose {comp}")
print(f"You Choose {pchoice}")


if output == None:
    print("Tie")
elif output == True:
    print("You Win!")
else:
    print("You Lose!")
