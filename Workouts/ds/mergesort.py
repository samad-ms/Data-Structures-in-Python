# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#         merge_sort(left)
#         merge_sort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i = i + 1
#                 k = k + 1
#             else:
#                 arr[k] = right[j]
#                 j = j + 1
#                 k = k + 1
#         while i < len(left):
#             arr[k] = left[i]
#             i = i + 1
#             k = k + 1
#         while j < len(right):
#             arr[k] = right[j]
#             j = j + 1
#             k = k + 1
#
#
# arr = [3, 2, 5, 1, 7, 8, 32, 67]
# merge_sort(arr)
# print(arr)


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i,j,k=0,0,0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i=i+1
                k=k+1
            else:
                arr[k] = right[j]
                j = j + 1
                k = k + 1

        while i<len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1


        while j<len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    return arr



arr=[43,54,23,135,32,64]
merge_sort(arr)
print(arr)






















