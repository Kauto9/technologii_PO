def sum_digits(number):
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    result = []
    for number in numbers:
        if -threshold <= number <= 0:
            result.append(number)
    return result
