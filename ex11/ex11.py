import csv
import sys

with open('{}/data.csv'.format(sys.path[0]), 'r') as fin:
    reader = csv.reader(fin, delimiter=' ')
    grid = [map(int, row) for row in reader]

product = 0
for row_num in range(20):
    for idx in range(16):
        # verticals
        if grid[idx][row_num] * grid[idx+1][row_num] * grid[idx+2][row_num] * grid[idx+3][row_num] > product:
            product = grid[idx][row_num] * grid[idx+1][row_num] * grid[idx+2][row_num] * grid[idx+3][row_num]

        # horizontals
        if grid[row_num][idx] * grid[row_num][idx+1] * grid[row_num][idx+2] * grid[row_num][idx+3] > product:
            product = grid[row_num][idx] * grid[row_num][idx+1] * grid[row_num][idx+2] * grid[row_num][idx+3]

#diags
for row_num in range(16):
    for idx in range(16):
        if grid[row_num][idx] * grid[row_num+1][idx+1] * grid[row_num+2][idx+2] * grid[row_num+3][idx+3] > product:
            product = grid[row_num][idx] * grid[row_num+1][idx+1] * grid[row_num+2][idx+2] * grid[row_num+3][idx+3]

for row_num in range(3, 20):
    for idx in range(16):
        if grid[row_num][idx] * grid[row_num-1][idx+1] * grid[row_num-2][idx+2] * grid[row_num-3][idx+3] > product:
            product = grid[row_num][idx] * grid[row_num-1][idx+1] * grid[row_num-2][idx+2] * grid[row_num-3][idx+3]

print product
