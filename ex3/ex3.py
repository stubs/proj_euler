#!/usr/bin/env python


def largest_prime_factor(in_numb):
    i = 2
    while i ** 2 < in_numb:
        while in_numb % i == 0:
            in_numb /= i
        i += 1

    return in_numb


print largest_prime_factor(12)
