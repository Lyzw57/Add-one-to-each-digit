def add_one_to_each(number):
    result = 0
    factor = 0

    while number:
        result += ((number % 10) + 1) * 10 ** factor
        if (number % 10) + 1 < 10:
            factor += 1
        else:
            factor += 2
        number //= 10

    return result