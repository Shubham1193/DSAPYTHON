def quickselect(data, lo, hi, k):
    pivot_index = partition(data, lo, hi)
    
    if pivot_index == k - 1:  # Adjust for 0-based indexing
        return data[pivot_index]
    elif pivot_index > k - 1:
        return quickselect(data, lo, pivot_index - 1, k)
    else:
        return quickselect(data, pivot_index + 1, hi, k)

def partition(data, lo, hi):
    pivot = data[hi]
    i = lo
    j = lo
    while i <= hi:
        if data[i] > pivot:
            i += 1
        else :
            data[i] , data[j] = data[j] , data[i]
            i += 1
            j += 1
    return j - 1

data = [8, 3, 5, 7, 6, 1, 4, 2]
k = 3
ans = quickselect(data, 0, len(data) - 1, k)
print(ans)  # Output: 3
