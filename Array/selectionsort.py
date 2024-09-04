def selectionsort(data) :
    # itr 1 select smallet and swpa with 1st elem 
    n = len(data)
    for i in range(n-1):
        min = i
        for j in range(i + 1 , n):
            if data[j] < data[min]:
                min = j
        data[i] , data[min] =  data[min] , data[i]
    return data

data = [5,9,8,2,1]
print("Unsorted List:", data)
data = selectionsort(data)
print("Sorted List:", data)