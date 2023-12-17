# این برنامه از کاربر یک کلمه دریافت میکند
# اگر زوج باشد دو حرف وسط ان و اگر فرد باشد حرف وسط ان را نمایش میدهد



def get_middle(s):

    if len(s) == 0:
        return False
    
    if len(s) > 1000:
        return False

    elif (len(s) == 1) or (len(s) == 2):
        return s
    
    # فرد
    elif len(s) > 2 and len(s) % 2 != 0:
        
        i = int(len(s)/2)

        return s[i]
    
    # زوج
    else:

        i = int(len(s)/2)

        return s[i-1] + s[i]


user_input = input("enter a word : ")
result = get_middle(user_input)

if result == False:
    print("you need to enter a word between (1_1000) char")

else:
    print(f"the middle char in {user_input} is --> {result}")