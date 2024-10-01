def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_arrays(left, right, arr)


def merge_two_arrays(a, b, arr):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [3, 0, 6, 1, 76, 23]
    merge_sort(arr)
    print(arr)
