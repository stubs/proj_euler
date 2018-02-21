#!/usr/bin/env python
from itertools import count, islice

def generate_nats(upper_limit):
    """generate list of natural numbers below upper_limit that are also multiples of 3 or 5"""
    return (x for x in xrange(int(upper_limit)) if (x % 3 == 0) or (x % 5 == 0))


def islice_generate_nats(upper_limit):
    """version I initially thought I would be able to pass in arbitrarily large integers...
    unfortunately stop argument for islice() must be None or an integer: 0 <= x <= maxint. """
    return (x for x in islice(count(), upper_limit) if (x % 3 == 0) or (x % 5 == 0))



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
         The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000""")
    parser.add_argument("--upper_limit",
                        help="Calculate the sum of natural numbers which are multiples of 3 or 5 below this upper limit integer",
                        required=True)
    args = parser.parse_args()

    print sum(generate_nats(args.upper_limit))
