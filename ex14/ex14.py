
def collatz_even(num):
    return num/2


def collatz_odd(num):
    return (3*num) + 1


def check_dict(dictionary, current_key, check_key):
    """if check_key already in dict stop and combine already computed list"""
    if dictionary.get(check_key):
        dictionary[current_key] += dictionary.get(check_key)
        return True
    else:
        dictionary[current_key].append(check_key)
        return False


collatz = dict()
for x in xrange(2, 1000001):
    if not collatz.get(x):
        collatz[x] = [x]
        y = x
        while y > 1:
            if y % 2 == 0:
                z = collatz_even(y)
                if check_dict(collatz, x, z):
                    break
            else:
                z = collatz_odd(y)
                if check_dict(collatz, x, z):
                    break
            y = z

length_dict = {key: len(value) for key, value in collatz.items()}
print max(length_dict, key=length_dict.get)
