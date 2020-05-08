def collatz(num, count):
    count += 1
    if num == 1:
        return count
    else:
        if num % 2 == 0:
            return collatz(num / 2, count)
        else:
            return collatz(3 * num + 1, count)

max_seq = 0
max_collatz = 0

import time
start = time.time()
for i in range(1, 1000000):
    max_len = collatz(i, 0)
    if max_len >= max_seq:
        max_seq = max_len
        max_collatz = i
end = time.time()

print(f"Max Sequence Length = {max_seq}")
print(f"Max Collatz Numbers = {max_collatz}")
print(f"Time Taken = {end - start} seconds")

