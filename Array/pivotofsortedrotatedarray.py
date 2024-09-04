def pivot(data):
    lo = 0
    hi = len(data) - 1

    while(lo < hi):
        mid = int((lo + hi) / 2)
        if(data[mid] < data[hi]):
            hi = mid
        else:
            lo = mid + 1
    return data[lo]

data = [5,4,3,1,2]

ans = pivot(data)
print(ans)