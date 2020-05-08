import time
import numpy as np


def sum_primes(up_bound):
    if up_bound < 2:
        return 0

    i = 1
    primes = np.array([2], dtype='int64')  # smallest prime number

    def is_prime(number, list_primes):
        number_arr = np.full(list_primes.size, number)
        remainders = np.remainder(number_arr, list_primes)
        if np.any(remainders == 0):
            return False
        return True

    while i < up_bound:
        i += 1
        if is_prime(i, primes):
            primes = np.append(primes, i)

    return sum(primes)


start = time.time()
print(sum_primes(2000000))
end = time.time()
print(f"Time taken = {end - start:.2f} seconds")

# sum_primes(1000000) [using lazy eval lists]
# 37550402023
# Time taken = 189.03 seconds

# sum_primes(1000000) [using np arrays]
# 37550402023
# Time taken = 254.31 seconds

