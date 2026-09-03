def game():
    import random

    user_dict = {
        "s": 1,
        "w": -1,
        "g": 0,
        "q": 2
    }

    reverse_dict = {
        1: "Snake",
        -1: "Water",
        0: "Gun",
        2: "Quit game"
    }

    user1_score = 0
    user2_score = 0

    # Read previous high score
    with open("CH 9/PRACTICE SET/Hi-score.txt", "r") as f:
        data = f.read()

    if data == "":
        high_score = 0
    else:
        high_score = int(data)

    # User 1
    while True:
        user1 = input("User 1 choice (s/w/g/q): ").lower()

        if user1 not in user_dict:
            print("Invalid input")
            continue

        if user1 == "q":
            print("User 1 quit the game.")
            print()
            print("Now turn is User 2")
            break

        user_num1 = user_dict[user1]
        computer = random.choice([1, -1, 0])

        print(f"User 1 choose {reverse_dict[user_num1]}")
        print(f"Computer choose {reverse_dict[computer]}")

        if user_num1 == computer:
            print("Draw")
            print()


        elif (computer - user_num1) == -1 or (computer - user_num1) == 2:
            print("User 1 lose")
            print()


        else:
            print("User 1 win")
            print()

            user1_score += 1

    # User 2
    while True:
        user2 = input("User 2 choice (s/w/g/q): ").lower()

        if user2 not in user_dict:
            print("Invalid input")
            continue

        if user2 == "q":
            print("User 2 quit the game.")
            break

        user_num2 = user_dict[user2]
        computer = random.choice([1, -1, 0])

        
        print(f"User 2 choose {reverse_dict[user_num2]}")
        print(f"Computer choose {reverse_dict[computer]}")

        if user_num2 == computer:
            print("Draw")
            print()


        elif (computer - user_num2) == -1 or (computer - user_num2) == 2:
            print("User 2 lose")
            print()


        else:
            print("User 2 win")
            print()

            user2_score += 1

    # Current game score
    score = max(user1_score, user2_score)

    print("\n===== FINAL SCORE =====")
    print(f"User 1 Score: {user1_score}")
    print(f"User 2 Score: {user2_score}")
    print(f"Current Score: {score}")
    print(f"Previous High Score: {high_score}")

    # Update high score
    if score > high_score:
        high_score = score

        with open("CH 9/PRACTICE SET/Hi-score.txt", "w") as f:
            f.write(str(f"The score is {high_score}"))

        print(f"NEW HIGH SCORE: {high_score}")
    else:
        print("High score not broken.")

    return score
score = game()
print(f"\nGame returned score: {score}")