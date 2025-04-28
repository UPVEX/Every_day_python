#quera_chalenge
#در این برنماه ابتدا یه سری اعداد میگیریم و انها رو به زوج و فرد تقسیم میکنیم


def separator(numbers):

    zooj = []
    fard = []

    for i in numbers:
        i = int(i)
        if i%2 == 0:
            zooj.append(i)
        else:
            fard.append(i)

    print("zooj are ==> ",zooj) 
    print("fard are ==> ",fard) 


numbers = (input("enter your numbers ==> "))
number_list = numbers.split()
print(separator(number_list))