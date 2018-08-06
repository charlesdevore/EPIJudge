from test_framework import generic_test


def reverse(x):
    # Reverse the order of a base 10 integer using bit-wise methods
    x_remaining = abs(x)
    sign = x // x_remaining
    x_result = 0

    while x_remaining:
        x_result = x_result * 10 + x_remaining % 10
        x_remaining //= 10

    return sign * x_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
