# Core Rules
# Snake vs. Water: Snake drinks the water, so Snake wins.
# Water vs. Gun: Gun drowns or is doused in water, so Water wins.
# Gun vs. Snake: Gun shoots and kills the snake, so Gun wins.
# Draw: If both players choose the same option, the round is a draw.

# Snake = 1
# Water = -1
# Gun = 0
import random

# Fix 1: Correct computer choices to match user values
computer = random.choice([1, -1, 0])

user = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

user_dict = {
    "s": 1,
    "w": -1,
    "g": 0
    }
reverse_dict = {
    1: "Snake",
    0: "Gun",
   -1: "Water"
}

if user not in user_dict:
    print("Invalid input!")
else:
    user_num = user_dict[user]
    print(
        f"User chose {reverse_dict[user_num]}\nComputer chose {reverse_dict[computer]}"
    )

    def check_who_win():
        if computer == user_num:
            print("Draw")
        # Fix 2: Explicit win conditions for cyclical rules
        # Snake (1) beats Water (-1)
        # Water (-1) beats Gun (0)
        # Gun (0) beats Snake (1)
        elif (
            (user_num == 1 and computer == -1)
            or (user_num == -1 and computer == 0)
            or (user_num == 0 and computer == 1)
        ):
            print("You win!")
        else:
            print("You lose!")

    check_who_win()