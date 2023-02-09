def high_and_low(numbers):
    split_numbers = list(map(int, numbers.split(" ")))
    min_n = min(split_numbers)
    max_n = max(split_numbers)
    numbers = str(max_n) + " " + str(min_n)
    return numbers