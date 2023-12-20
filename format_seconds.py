# این برنامه از کاربر یک ثانیه میگیرد و فورمت ان را عوض میکند و به صورت ساعت و دقیقه و ثانیه بر میگرداند


def format_seconds(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input must be a non-negative integer less than or equal to 359999")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


user_input = int(input("please enter your number : "))

print ("output: ", format_seconds(user_input))
