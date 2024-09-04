def quicksort(data, lo, hi):
    if lo >= hi:
        return  # Base case: empty or single-element subarray

    pivot = data[hi]
    pi = partition(data, pivot, lo, hi)

    quicksort(data, lo, pi - 1)
    quicksort(data, pi + 1, hi)
    return data

def partition(data, pivot, lo, hi):
    i = lo
    j = lo
    while i <= hi:
        if data[i] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
            j += 1
        else:
            i += 1

    return j - 1  # Return the final index of elements less than the pivot

data = [4, 6, 7, 1, 2, 4, 5, 1, 3]
print(quicksort(data, 0, len(data) - 1))