"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, (num // 2) + 1, 2):
        if num % i == 0:
            return False   
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'x = {number_of_primes} should have been a positive number.')
    else:
        list = []
        count = 2
        while len(list) < number_of_primes:
            if is_prime(count):
                list.append(count)
            count += 1
        return list
