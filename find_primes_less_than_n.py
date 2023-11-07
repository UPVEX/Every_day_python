# این برنامه یک ورودی میگیرد و تمام اعداداول قبل از ورودی رو چاپ میکند

def aval(n):

    accumulator = 0

    for i in range(1, n+1):

        if n % i == 0:
            accumulator+=1

    if accumulator == 2:
        return True
    else:
        return False


def find_primes_less_than_n(n):

    prime_num = []
    
    for i in range(2, n+1):
        if aval(i):
            prime_num.append(i)

    return prime_num


number = int(input("enter a number for lower prime num -> "))

print("the prime number less than ",number ," is -> ", find_primes_less_than_n(number))


