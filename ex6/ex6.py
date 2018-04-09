#!/usr/bin/env python


def sum_squares(upper_limit):
    return sum([x**2 for x in range(upper_limit + 1)])


def square_sum(upper_limit):
    return (upper_limit * (upper_limit + 1)/2)**2


print square_sum(100) - sum_squares(100)

