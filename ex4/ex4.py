#!/usr/bin/env python

nums = range(100, 1000)
nums_set = {a * b for a in nums for b in nums}
print max(i for i in nums_set if str(i) == str(i)[::-1])
