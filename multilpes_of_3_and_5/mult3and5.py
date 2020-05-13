import sys

sys.setrecursionlimit(2000)


def m35(x):
    x -= 1

    def count35(num, total=0):
        if num == 0:
            return total
        elif any((num % 3 == 0, num % 5 == 0)):
            return count35(num-1, total + num)
        else:
            return count35(num-1, total)

    return count35(x)


print(m35(1000))

