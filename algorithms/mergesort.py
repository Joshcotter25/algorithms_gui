
def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], ascending)
    right = merge_sort(arr[mid:], ascending)
    return _merge(left, right, ascending)


def _merge(left, right, ascending):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if (left[i] <= right[j]) if ascending else (left[i] >= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # add remaining items
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged