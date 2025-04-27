#quera_chalenge
#یک اسانسور داریم که دکمه بالا و پایین فقط داره. ما باید از کاربر 4 تا دکمه رو بگیریم و در خروجی بگیم در کدوم طبقه پیاده میشه
#مثال اگر کاربر بزنه UUUDیعنی سه طبقه بالا میرود و یک طبقه پایین میاید و باید در خروجی 2 برگردانده شود




def calculate_floor(string):
    count = 0

    if len(string) == 4:

        for i in string:
            if i == 'U':
                count = count + 1

            elif i == 'D':
                count = count -1

            else:
                print("the elavator just accept U and D ")

        return count

    else:    
        print("EROR: you just can enter 4 times")
        


string = str(input("please enter U and D for 4 time ==> "))

print(calculate_floor(string))