#این برنامه بازی سنگ کاغذ قیچی رو شبیه سازی میکنه 

import random

print("welcome to this game(ROCK_PAPER_SCISSOR)")
print("Please enter how many rounds do you want to play")
print("(for ex:if you chose 5, each pearson reach 5 round win the game)")


while True:
    try:
        round = int(input("==> : "))
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")



pc_ai_point = 0
user_point = 0

while pc_ai_point != round and user_point != round:

    pc_ai =random.randint(1, 3)
    user = int(input("please chose (1:sang , 2:kaghaz , 3:gheichi) ==>"))

    if user == pc_ai:
        print("system choise is ", pc_ai)
        print("tie")
        print("result ==> computer: ", pc_ai_point," __ user: ",user_point)
        
    elif ((user == 1 and pc_ai == 3) or (user == 2 and pc_ai == 1) or (user == 3 and pc_ai == 2)):
        print("system choise is ", pc_ai)
        user_point = user_point + 1
        print("you win this round")
        print("result ==> computer: ", pc_ai_point," __ user: ",user_point)

    else:
        print("system choise is ", pc_ai)
        pc_ai_point = pc_ai_point + 1
        print("you lose this round")
        print("result ==> computer: ", pc_ai_point," __ user: ",user_point)


if pc_ai_point > user_point:
    print("**********************************")
    print("  ***YOU WIN THE GAME***")
    print("result ==> computer: ", pc_ai_point," __ user: ",user_point)

else :
    print("**********************************")
    print("  ***YOU WIN THE GAME***")
    print("result ==> computer: ", pc_ai_point," __ user: ",user_point)
        
