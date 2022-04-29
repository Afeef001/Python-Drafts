from msvcrt import getch
import random

print("Choose any of these, Rock(r), Paper(p), Scissors(s)")
score = 0

#----Rules----
#....1- Rock > Scissors....
#....2- Scissors > Paper....
#....3- Paper > Rock....


while True:
#....Taking User Input....
    player = input("(r/p/s)--->").lower()

#....Taking Computer input....
    guess = random.choice(["r", "p", "s"])
    
    if (player == "r" and guess == "s") or (player == "s" and guess == "p") or (player == "p" and guess == "r"):
        print(guess)
        print("You won!!")
        score += 1
    elif player == guess:
        print(guess)
        print("Tie!!!")
    elif player not in ["r", "p", "s"]:
        print("!--invalid input--!")
    else:
        print(guess)
        print("You lose!!")
        print("Your Score: ", score)
        break

getch()