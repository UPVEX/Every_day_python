#این برنامه هر استرینگی رو معکوس میکند و در خروجی نمایش میدهد 

def reverse(input_string):

    reverse_string = ""

    for char in input_string:

        reverse_string = char + reverse_string
    return reverse_string


input_string = str(input("please enter your string here for reverse -> ")) 
print(reverse(input_string))