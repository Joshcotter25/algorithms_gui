from algorithms.mergesort import merge_sort

def min_max(arr):
    if not arr:
        raise ValueError("Array is empty.")
    mn = mx = arr[0]
    for x in arr[1:]:
        if x < mn: mn = x
        if x > mx: mx = x
    return mn, mx

def mode(arr):
    if not arr:
        raise ValueError("Array is empty.")
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    max_count = 0
    for v in freq.values():
        if v > max_count:
            max_count = v
    if max_count == 1:
        return []  # "no mode" case
    return [k for k, v in freq.items() if v == max_count]

def median(sorted_arr):
    n = len(sorted_arr)
    if n == 0:
        raise ValueError("Array is empty.")
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_arr[mid])
    return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0

def quartiles(arr):
    s = merge_sort(arr, ascending=True)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        lower = s[:mid]
        upper = s[mid:]
    else:
        lower = s[:mid]
        upper = s[mid+1:]
    q1 = median(lower)
    q3 = median(upper)
    return q1, q3, s

def stats_summary(arr):
    if not arr:
        raise ValueError("Array is empty.")
    mn, mx = min_max(arr)
    q1, q3, s = quartiles(arr)
    return {
        "smallest": mn,
        "largest": mx,
        "mode": mode(arr),
        "median": median(s),
        "q1": q1,
        "q3": q3,
        "sorted": s,
    }