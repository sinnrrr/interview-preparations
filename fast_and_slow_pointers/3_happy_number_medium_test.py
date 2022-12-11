"""
Any number will be called a happy number if, after repeatedly replacing it with
a number equal to the sum of the square of all of its digits, leads us to
number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
they will be stuck in a cycle of numbers which does not include ‘1’.
"""


import pytest


def find_happy_number_iterative(num: int):
    history = []
    digits_pow_sum = num

    while digits_pow_sum != 1:
        if digits_pow_sum in history:
            return False

        current = digits_pow_sum
        digits_pow_sum = _digit_calcs(current)
        history.append(current)

    return True


def _digit_calcs(num: int) -> int:
    digits = [int(d) for d in str(num)]
    digits_pow_sum = sum([d**2 for d in digits])

    return digits_pow_sum


def find_happy_number(num: int):
    ptr1 = ptr2 = num

    while True:
        ptr1 = digit_square_sum(ptr1)
        ptr2 = digit_square_sum(digit_square_sum(ptr2))

        if ptr1 == 1 or ptr2 == 1:
            return True

        if ptr1 == ptr2:
            return False


def digit_square_sum(num):
    sum = 0
    while num != 0:
        d = num % 10
        num //= 10
        sum += d**2
    return sum


@pytest.mark.parametrize("num,expected", [(23, True), (12, False)])
def test(num, expected):
    assert find_happy_number(num) == expected
