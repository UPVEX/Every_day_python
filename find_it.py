# برنامه زیر یک تایعی است که به عنوان ورودی یک ارایه عددی میگیره عددی که به تعداد فرد بار تکرار شده باشه رو بر میگردونه
# codewars challenge
# https://www.codewars.com/kata/54da5a58ea159efa38000836



def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i