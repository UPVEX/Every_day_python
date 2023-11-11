# این برنامه دو تا ورودی از کاربر میگیرد یکی از انها لیست کلی اعداد است و دیگری یک لیست اعداد دیگر است
# این برنامه چک میکند که ایا در لیست اول لیست دوم وجئد دارد یا خیر / اگر بله در کدام ایندکس 


def find_sequence(lst, sequence):

    for i in range(len(lst) - len(sequence) + 1):
        if lst[i:i+len(sequence)] == sequence:
            return True, i
    return False, None


user_input_list = input("please enter  your list number ==> ")
user_input_sequence = input("please enter your list number that you want to search in real list ==> ")


numbers_list = [int(num) for num in user_input_list.split()]
sequence_list = [int(num) for num in user_input_sequence.split()]


exists, index = find_sequence(numbers_list, sequence_list)


if exists:
    print("the list has sequence and it is in the ", index, " index")
else:
    print("***sequence is not in list***")
