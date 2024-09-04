def mergesort(data , lo , hi):
    if (lo == hi):
        ba = [data[lo]]
        return ba
    
    mid = (lo + hi)/2
    fsh = mergesort(data, lo , mid)
    ssh = mergesort(data , mid + 1 , hi)
    fsa = mergetwosortedarray(fsh , ssh)
    return fsa

def mergetwosortedarray(arr1 , arr2):
    ans = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.push(arr1[i])
        else :
            ans.push(arr2[j])
    while i < len(arr1):
        ans.push(arr1[i])
    while j < len(arr2):
        ans.push(arr2[j])
    return ans

data = [4,2,6,7,1,0,9]
ans = mergesort(data , 0 , len(data))
print(ans)