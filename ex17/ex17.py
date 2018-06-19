from num2words import num2words

total = 0
for dig in range(1, 1001):
    for i in num2words(dig):
        if i not in [" ", "-"]:
            total += 1
print(total)

