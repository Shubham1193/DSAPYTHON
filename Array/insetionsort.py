# def insertionSort(data):
#     n = len(data)
#     for i in range(1 , n):
#         # key = i
#         j = i - 1
#         while j >= 0 and data[j] > data[j+1] : 
#             data[j] ,data[j+1] = data[j+1] , data[j]
#             j = j - 1
#     return data
# data = [5,9,8,2,1]
# # data = [2,5,8,9,1]
# print("Unsorted List:", data)
# data = insertionSort(data)
# print("Sorted List:", data)

def insertionSort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:   # data = [2,5,8,9,6]  last elem eg save 6 9 comes to 6 8 comes to 9 and 6 comes to 8
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
    return data

data = [5, 9, 8, 2, 1]
print("Unsorted List:", data)
data = insertionSort(data)
print("Sorted List:", data)
