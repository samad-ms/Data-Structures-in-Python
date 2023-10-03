def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[largest]:
        largest=left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
def heap_sort(arr):
    n=len(arr)
    for i in range(((n-2)//2),-1,-1):
        heapify(arr,n,i)
    print(arr)

    min_val=float("inf")
    for i in range(n-1,(n-2)//2,-1):
        cur_val=arr[i]
        min_val=min(cur_val,min_val)
    return min_val


num=[5,16,8,14,20,1,26]
heap_sort(num)
print(num)