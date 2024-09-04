def targetPairsum(data , target):
    n = len(data)
    l = 0
    r = n-1
    ans = []
    while(l < r):
        if (data[l] + data[r] > target):
            r -= 1
        elif (data[l] + data[r] < target):
            r += 1
        else :
            ans.append([l , r])
            l += 1
            r -= 1
    return ans

ans = targetPairsum([2 , 3 , 4 , 5 , 6 , 7] , 8)
print(ans)