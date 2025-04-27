# یک سرگرمی ساده :)





import random

adad = random.randint(1,101)

t = int(input("test your chance to say anumber"))

while(t != adad):

    if t>adad :
        print("please enter smaller number")
        t = int(input("test your chance to say anumber"))

    elif t<adad :
        print("please enter biger number")
        t = int(input("test your chance to say anumber"))

print("yes my number was ",adad)
