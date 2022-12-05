import math

n = 16  # size of the square matrix
m = 10  # number of received batch size

example = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [3, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [4, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [5, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [6, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [8, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [12, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [13, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [14, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [15, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [16, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16],
    [11, 12, 13, 14, 15, 16]
]

x_size = math.ceil(n/m)
print(x_size)

y_partitions = [m for i in range(math.floor(n/m))]
if n % m:
    y_partitions.append(n % m)
print(y_partitions)


def getShiftedIndex(base_index, m, x_size):
    result = [base_index]
    next_index = base_index
    for _ in range(x_size-1):
        next_index += m
        result.append(next_index)
    return result


def getMergedLists(input, rows):
    result = []
    for i in rows:
        result += input[i]
    return result


row_index = 0
output = []
for i in y_partitions:
    for _ in range(i):
        row = getMergedLists(example, getShiftedIndex(row_index, i, x_size))
        print(row)
        output.append(row)
        row_index += 1
    row_index += i*(x_size-1)
