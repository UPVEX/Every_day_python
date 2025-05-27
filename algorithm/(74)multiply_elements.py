# این  برنامه حاصل ضرب لیست های متناظر رو در خروجی نمایش میده



def multiply_elements(list1, list2):
    
    len_list1 = len(list1)
    len_list2 = len(list2)

    result_list = []

    min_len = min(len_list1, len_list2)

    for i in range(min_len):
        result_list.append(list1[i] * list2[i])

    return result_list


input_list1 = [1, 2, 3, 4]
input_list2 = [5, 6, 7, 8]

result = multiply_elements(input_list1, input_list2)
print(result)
