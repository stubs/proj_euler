#!/usr/bin/env python

nums = range(100, 1000)

# no need to compute a * b AND b * a
nums_set = {a * b for a in nums for b in nums if a <= b and str(a * b) == str(a * b)[::-1]}

print max(nums_set)

