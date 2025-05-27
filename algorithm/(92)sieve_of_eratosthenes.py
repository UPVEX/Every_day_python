"""

Your task is to write a function that takes two integers n, m and returns a sorted array of all integers from n to m inclusive, which have only 3 divisors (1 and the number itself excluded).

Example:
solution(2, 20) -> [16]
16 has 3 divisors: 2, 4, 8 (1 and 16 aren't included)

Input:
n - integer (2 ≤ n ≤ 10^10)
m - integer (20 ≤ m ≤ 10^18)

Output:
result - array of integers

"""



import math

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]

def solution(n, m):
    result = []
    max_p = int(m**0.25)  # because p^4 <= m, so p <= m^(1/4)
    primes = sieve_of_eratosthenes(max_p)

    for p in primes:
        p4 = p**4
        if n <= p4 <= m:
            result.append(p4)

    return sorted(result)

# مثال استفاده
print(solution(2, 20))  # خروجی: [16]
