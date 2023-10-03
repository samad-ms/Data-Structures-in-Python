def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr




# def delete_common_elements(array1, array2):
#     hash_set = set(array1)
#     for element in array2:
#         if element in hash_set:
#             hash_set.remove(element)
#
#     return list(hash_set)
#
#
# # Example usage
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [4, 5, 6, 7, 8]
# result = delete_common_elements(arr1, arr2)
# print(result)
