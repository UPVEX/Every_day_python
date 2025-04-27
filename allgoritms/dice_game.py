#در این بازی تعداد دفعاتی که میخواهد تاس بیندازد رو به عنوان ورودی میدهد
# این برنامه در هر دفعه دو بار تاس میریزد و انها را جمع کرده و به عنوان امتیاز ذخیره میکند
# اما اگر در هر دفعه تاس انداختن ورودی ها یکی باشد امتیاز کاربر صفر میشود و بازی همانجا تمام است



import random

def dice_game(rolls):

    score = 0
    

    for roll in rolls:

        if roll[0] == roll[1]:
            score = 0
            break

        else:
            print(roll[0] , "+", roll[1], " ==> ", roll[0] + roll[1])
            score = score + (roll[0] + roll[1])
            
            
    return score


def generate_random_dice_rolls(num_rolls):

    rolls = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(num_rolls)]

    return rolls


num_rolls = int(input("please enter how many rolls do you want to play ==> ") )  

rolls = generate_random_dice_rolls(num_rolls)
print(rolls)

result = dice_game(rolls)
print(result)
