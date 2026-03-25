def quick_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr

    pivote = arr[0]

    if reverse:
        menores = [x for x in arr[1:] if key(x) > key(pivote)]
        mayores = [x for x in arr[1:] if key(x) <= key(pivote)]
    else:
        menores = [x for x in arr[1:] if key(x) < key(pivote)]
        mayores = [x for x in arr[1:] if key(x) >= key(pivote)]

    return quick_sort(menores, key, reverse) + [pivote] + quick_sort(mayores, key, reverse)


def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)


def merge(left, right, key, reverse):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if reverse:
            if key(left[i]) > key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if key(left[i]) < key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr, key=lambda x: x, reverse=False):
    arr = arr.copy()

    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1

        while j >= 0 and (
            (key(arr[j]) < key(actual) if reverse else key(arr[j]) > key(actual))
        ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = actual

    return arr