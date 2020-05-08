import time


def collatz_memo(num):
    cache = {}

    def collatz(n, c):
        n = int(n)
        mem = cache.get(n)
        if mem:
            return mem
        else:
            c += 1
            if n == 1:
                result = c
            else:
                if n % 2 == 0:
                    result = collatz(n / 2, c)
                else:
                    result = collatz(3 * n + 1, c)
            cache[n] = result
            return result
    return collatz(num, 0)


def answer(max_range):
    max_seq = 0
    max_collatz = 0
    for i in range(1, max_range):
        max_len = collatz_memo(i)
        if max_len > max_seq:
            max_seq = max_len
            max_collatz = i

    print(f"Max Sequence Length = {max_seq}")
    print(f"Max Collatz Numbers = {max_collatz}")


start = time.time()
answer(1000000)
end = time.time()
print(f"Time Taken = {end - start} seconds")


