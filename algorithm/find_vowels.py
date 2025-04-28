# برنامه زیر تعداد حروف صدا دار را در جمله ورودی میشمارد



def get_count(sentence):
    
    vowels = 'aeiou'
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count
    
user_input = input("write your sentence : ")

result = get_count(user_input)

print(f"({user_input}) has {result} vowels alfabet")