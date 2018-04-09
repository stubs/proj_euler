def gcd(a, b):
    """Euclid's thing"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def reduced_lcm(*args):
    return reduce(lcm, args)

