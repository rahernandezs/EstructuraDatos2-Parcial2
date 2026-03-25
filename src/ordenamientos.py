def quick_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr

    pivote = arr[0]
    menores = [x for x in arr[1:] if key(x) < key(pivote)]
    iguales = [x for x in arr if key(x) == key(pivote)]
    mayores = [x for x in arr[1:] if key(x) > key(pivote)]

    if reverse:
        return quick_sort(mayores, key, reverse) + iguales + quick_sort(menores, key, reverse)
    else:
        return quick_sort(menores, key, reverse) + iguales + quick_sort(mayores, key, reverse)


def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)


def merge(left, right, key, reverse):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (key(left[i]) < key(right[j]) and not reverse) or (key(left[i]) > key(right[j]) and reverse):
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


def insertion_sort(arr, key=lambda x: x, reverse=False):
    arr = arr.copy()

    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1

        while j >= 0 and ((key(arr[j]) > key(actual) and not reverse) or (key(arr[j]) < key(actual) and reverse)):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = actual

    return arr