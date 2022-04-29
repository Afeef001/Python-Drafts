from msvcrt import getch
import random

print("---Rules---\n You can Score 0 to 6 at a time")


p_score = 0
c_score = 0

while True:
    player = int(input("(P)--->"))

    computer = random.choice([0, 1, 2, 3, 4, 5, 6])
    print("(C)--->", computer)

    if player != computer :
        p_score += player
    else:
        print("---It's an out---")
        print("----Now it's computer's turn----")
        while c_score <= p_score:
            player = int(input("(P)--->"))

            computer = random.choice([0, 1, 2, 3, 4, 5, 6])
            print("(C)--->", computer)

            if player != computer:
                c_score += computer
            else:
                print("---It's an out---")
                break
        break

if p_score > c_score:
    print(f"Computer vs Player : {c_score}/{p_score}")
    print("Hurray!! The Player is the winner")
elif p_score < c_score:
    print(f"Computer vs Player : {c_score}/{p_score}")
    print("Yahoo!! The Computer is the winner")
else:
    print(f"Computer vs Player : {c_score}/{p_score}")
    print("Aww!! it's a tie...Better Luck Next Time...")

getch()