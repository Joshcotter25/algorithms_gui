
def selection_sort(arr, ascending=True):
    a = arr[:]
    n = len(a)

    for i in range(n):
        best = i
        for j in range(i + 1, n):
            if (a[j] < a[best]) if ascending else (a[j] > a[best]):
                best = j
        a[i], a[best] = a[best], a[i]

    return a


def bubble_sort(arr, ascending=True):
    a = arr[:]
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a