def sort012(data):
    i = 0
    j = 0
    k = len(data) - 1
    while(i < k):
        if data[i] == 1:
            i = i + 1
        elif data[i] == 2 :
            data[i] , data[k] = data[k] , data[i]
            k = k - 1
        elif data[i] == 0 :
            data[i] , data[j] = data[j] , data[i]
            i = i + 1
            j = j + 1 
    return data

ans = sort012([1,1,2,0,2,2,1,1,0,0,2])
print(ans)
