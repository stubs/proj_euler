#!/usr/bin/env python


def squares_array(upper_limit):
    return [x for x in range(upper_limit)]


def sum_squares(upper_limit):
    return sum([x**2 for x in squares_array(upper_limit)])


def square_sum(upper_limit):
    return sum(squares_array(upper_limit))**2


print square_sum(101) - sum_squares(101)

