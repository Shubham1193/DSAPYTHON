def mergearray(data1, data2):
    ans = []
    i = 0
    j = 0

    while i < len(data1) and j < len(data2):
        if data1[i] < data2[j]:
            ans.append(data1[i])
            i += 1
        else:
            ans.append(data2[j])
            j += 1

    # Append remaining elements of data1, if any
    while i < len(data1):
        ans.append(data1[i])
        i += 1

    # Append remaining elements of data2, if any
    while j < len(data2):
        ans.append(data2[j])
        j += 1

    return ans

# Example usage
data1 = [1, 3, 5]
data2 = [2, 4, 6 , 9]
merged_data = mergearray(data1, data2)
print("Merged Array:", merged_data)
