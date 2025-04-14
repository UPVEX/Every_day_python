# برنامه زیر سه حالت دارد
#رمز گشایی با روش سزار
# رمز گزاری با روش سزار 
# پیدا کردن رمز گشایی بدون  داشتن کلید 



from string import ascii_letters



def encrypt(string, key):
    
    alpha = ascii_letters
    result = ''

    for ch in string:

        if ch not in alpha:
            result += ch 
        else:
            new_key = (alpha.index(ch) + key) % 52
            result += alpha[new_key]
    
    return result




def decrypt(string, key):
    key *= -1
    return encrypt(string, key)




def brute_force(string):
    alpha = ascii_letters
    key = 1
    result = ''
    brute_force_data = {}

    while key <= len(alpha):
        result += decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    
    return brute_force_data



print('press 1 for Encrypt')
print('press 2 for Decrypt')
print('press 3 for BRUTE FORCE')

user_selection = int(input("enter your choice ---> "))

if user_selection == 1:
    print("....................")
    string = str(input("please enter your text to encrypt by CASEAR method --> "))
    key = int(input('please enter your key(1-52)'))

    if key>52:
        print("***INVALID***")
    else:
        print("....................")
        print(f"encrypted password for ({string}) is --> {encrypt(string, key)}")


elif user_selection == 2:
    print("....................")
    string = str(input("please enter your text to decrypt by CASEAR method --> "))
    key = int(input('please enter your key(1-52)'))

    if key>52:
        print("***INVALID***")
    else:
        print("....................")
        print(f" ({string}) unlocked --> {decrypt(string, key)}")


elif user_selection == 3:
    print("....................")
    string = str(input("please enter your encrypted text to find the answer by CASEAR method --> "))
    print("....................")

    brute = brute_force(string)
    for key, value in brute.items():
        print(f"{key}: {value}")

else:
    print("....................")
    print("***Invalid Input***")