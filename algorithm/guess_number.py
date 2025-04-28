# این برنامه یک بازی را اجرا میکنه که کاربر باید عددی که کامپیوتر ساخته را حدث بزنه



import random

def guess_the_number():
    print("<<guess the number>> ")
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("enter your guess (0_100) --> "))
        attempts += 1

        if user_guess == target_number:
            print(f"you WIN . you found {target_number} in {attempts} time .")
            break
        elif user_guess < target_number:
            print("try guess <<larger>> number !!!")
            print("............................")
        else:
            print("try guess <<lower>> number !!!")
            print("............................")

guess_the_number()

