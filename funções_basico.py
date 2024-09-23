def multply_2(*args):
    accumulator = 1
    for i in args:
        accumulator *= i
    return accumulator


def even_odd(x):
    even_odd_var = f'{x} is even' if x % 2 == 0 else f'{x} is odd.'
    return even_odd_var


numbers = 1, 2, 3


print(multply_2(*numbers))
print(even_odd(3))