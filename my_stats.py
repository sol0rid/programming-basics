# my_stats.py
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

# my_stats.py
def minimum(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest