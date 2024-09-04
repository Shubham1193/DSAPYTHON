def bubble_sort(data):
  n = len(data)
  for i in range(n-1):
    for j in range(n-i-1):
      if data[j] > data[j+1]:
        data[j] , data[j+1] = data[j+1] , data[j]
  return data

# Example usage
data = [5,9,8,2,1]
print("Unsorted List:", data)
data = bubble_sort(data)
print("Sorted List:", data)

# itr one 5 with 9 , 9 with 8  swap , 9 , 2 swap 9 1 swap reached end  j = 0 1 2 3  