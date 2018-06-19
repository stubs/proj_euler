from math import sqrt


def pascal(n):
    r1, r2 = [1], [1, 1]
    while True:
        print(r1)
        if int(len(r1)/2) == sqrt(n**2):
            print(max([1] + [sum(pair) for pair in zip(r1, r1[1:]) ] + [1]))
            return True
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
