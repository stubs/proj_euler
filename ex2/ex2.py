#!/usr/bin/env python

def generate_fibs_ln(upper_limit):
    """generate fib seq where list items are not to exceed upper_limit (Linear time)"""
    seed_1 = 0
    seed_2 = 1
    fibs = list()

    while sum((seed_1, seed_2)) < upper_limit:
        fibs.append(sum((seed_1, seed_2)))
        seed_1 = seed_2
        seed_2 = fibs[-1]
    return fibs


print sum(x for x in generate_fibs_ln(4000000) if x % 2 == 0)           # correct

