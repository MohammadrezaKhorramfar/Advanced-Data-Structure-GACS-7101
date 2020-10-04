from math import ceil


def FindMaxInColumn(arr, rows, mid, max):
    max_index = 0
    for i in range(rows):
        if max < arr[i][mid]:
            max = arr[i][mid]
            max_index = i

    return max, max_index


def FindMaxInMatrix(arr, rows, columns, mid):
    max = 0
    max, max_index = FindMaxInColumn(arr, rows, mid, max)

    if mid == 0 or mid == columns - 1:
        return max

    if (max >= arr[max_index][mid - 1] and
            max >= arr[max_index][mid + 1]):
        return max

    if max < arr[max_index][mid - 1]:
        return FindMaxInMatrix(arr, rows, columns,
                               mid - ceil(mid / 2))

    return FindMaxInMatrix(arr, rows, columns,
                           mid + ceil(mid / 2))


def FindMaxMatrix(arr, rows, columns):
    return FindMaxInMatrix(arr, rows,
                           columns, columns // 2)


arr = [[7, 8, 9, 10, 9, 8, 7],
       [8, 9, 10, 11, 10, 9, 8],
       [9, 10, 11, 12, 11, 10, 9],
       [10, 11, 12, 13, 12, 11, 10],
       [9, 10, 11, 12, 11, 10, 9],
       [8, 9, 10, 11, 10, 9, 8],
       [7, 8, 9, 10, 9, 8, 7]]

rows = 7
columns = 7
print(FindMaxMatrix(arr, rows, columns))
