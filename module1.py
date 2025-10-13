def find_two_smallest(numbers):
    a = numbers[0]
    b = numbers[1]
    if a > b:
        a, b = b, a

    for x in numbers[2:]:
        if x < a:
            b = a
            a = x
        elif x < b:
            b = x

    return a, b
