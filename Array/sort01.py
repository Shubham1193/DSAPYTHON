def sort01(data):
    n = len(data)
    i = 0
    j = 0
    while(i < n):
        if data[i] == 1:
            i = i + 1
        else : 
            data[i] , data[j] = data[j] , data[i]
            i = i + 1
            j = j + 1
    return data

ans = sort01([1,1,0,1,0,1,1,0,1,0,0,0,1])
print(ans)