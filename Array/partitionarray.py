def partitionarray(data, p):
    i = 0
    j = 0
    n = len(data) - 1
    while (i <= n):
        if data[i] > p:
            i += 1
        elif data[i] <= p:
            data[i], data[j] = data[j], data[i]
            i += 1
            j += 1
    return data, j - 1  

ans = partitionarray([7,9,4,8,3,6,2,1] , 6)
print(ans)