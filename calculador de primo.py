import math
Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
max_prime = Primes[-1]

def prime_calculator(value):
    n = math.floor(value**(1/2))
    i = n

    while i > max_prime:
        is_prime = True
        for prime in Primes:
            if i != prime and i % prime == 0:
                is_prime = False
                break
        if is_prime:
            Primes.append(i)
        i -= 1

    flag = True
    for prime in Primes:
        if value != prime and value % prime == 0:
            flag = False
            return flag

    Primes.append(value)
    return flag

num = 36788
if prime_calculator(num):
    print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")