# این برنامه یک بازی حدث عدد هستش که لینک توضیحاتش  رو میزارم براتون
# https://backendbaz.ir/practice/pr-10261/python/

import random

def guess_the_number():
    player_name = input("Enter your name: ")
    print("Welcome,", player_name, "!")

    while True:
        computer_number = random.randint(1, 99)
        max_attempts_easy = 10
        max_attempts_hard = 7
        level = input("Choose the level (easy/hard): ").lower()

        if level == 'easy':
            max_attempts = max_attempts_easy
        elif level == 'hard':
            max_attempts = max_attempts_hard
        else:
            print("Invalid level. Please choose 'easy' or 'hard'.")
            continue

        print(player_name, ", try to guess the computer's number!")

        for attempt in range(1, max_attempts + 1):
            print("Attempt", attempt, "/", max_attempts)
            guess = int(input("Enter your guess (between 1 and 99): "))
            
            if guess < computer_number:
                print("Too low! Try a higher number.")
            elif guess > computer_number:
                print("Too high! Try a lower number.")
            else:
                print(f"********** {player_name}: You are a winner! **********")
                break

            if attempt == max_attempts:
                print(f"---------- {player_name}: You are out of attempts! ----------")
                print(f"The correct number was: {computer_number}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break


guess_the_number()

