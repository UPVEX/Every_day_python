# این یک بازی دیگه هستش که اینجا کامپیوتر عدد رو حدث باید بزنه . دقیقا برعکس مثال قبلی . توضیحات در لینک زیر
# https://backendbaz.ir/practice/pr-12286/python/

import random

def computer_guess():
    low, high = 1, 99
    attempts = 0

    while True:

        computer_guess = random.randint(low, high)
        print("Computer's guess: ", computer_guess)

        print("is your number: ", computer_guess)
        user_answer = input("(yes/no)")

        if user_answer == "yes":
            print("*** computer is win --- number is: " , computer_guess, "***")
            break

        elif user_answer == "no":
            user_feedback = input("computer guess up(u) or down(d): ")

            if user_feedback == "u":
                low = computer_guess + 1
            elif user_feedback == "d":
                high = computer_guess - 1
            else:
                print("Invalid input. Please enter 'u' for up or 'd' for down.")
                continue

            attempts += 1



    print("Number of attempts: ", attempts)


print("chose a number between 1 and 99 in your mind : ")
computer_guess()
