from itertools import combinations_with_replacement
import time


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def prod_palindrome(tup):
    return is_palindrome(tup[0] * tup[1])


def max_palindrome(digits):
    assert(type(digits) == int)
    min_num = int('1' + '0' * (digits - 1))
    max_num = int('9' * digits)
    numbers = combinations_with_replacement(range(min_num, max_num), 2)
    valid_prod = filter(prod_palindrome, numbers)
    max_prod = 0
    result_x = 0
    result_y = 0
    for el in valid_prod:
        product = el[0] * el[1]
        if product > max_prod:
            max_prod = product
            result_x, result_y = el[0], el[1]

    return max_prod, result_x, result_y


start = time.time()
maximum, x, y = max_palindrome(3)
end = time.time()
total_time = end - start

print(f"Max palindrome = {maximum}")
print(f"Product of {x} and {y}")
print(f"Time taken = {total_time:.2f} seconds")
