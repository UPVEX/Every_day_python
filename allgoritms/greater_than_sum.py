#برای هر عدد در لیست ورودی، بررسی کنید که آیا آن عدد از مجموع همه اعدادی که قبل از آن در لیست ظاهر می‌شوند بیشتر است یا خیر 
#اگر همه اعداد موجود در لیست در این شرط صدق می کردند، True برگردانید و در غیر این صورت False برگردانید


def greater_than_sum(numbers):

    for i in range(1, len(numbers)):

        if numbers[i] <= sum(numbers[:i]):
            return False
        
    return True


input_number = input("please enter your numbers by using space ==> ")
numbers = [int(num) for num in input_number.split()]

result = greater_than_sum(numbers)

print("result for your number ", numbers, " is ==> ", result)
