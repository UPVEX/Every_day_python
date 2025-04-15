"""
این برنامه یک لیست میگیرد و مینیمم ان را برمیگرداند و از لیست اصلی حذف میکند

   [4, 5, 2, 8, -2, 5, 1, 9] ==> -2
"""

def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:
        return stack

    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storage_stack.append(val)

    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min:
            stack.append(val)

    return stack, min


print(remove_min([4, 5, 2, 8, -2, 5, 1, 9]))
