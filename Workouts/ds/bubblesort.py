def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        print("working of out_loop",i+1,"times<<<<")
        swap=0
        for j in range(n-1-i):
            print("working of inner_loop", j + 1, "times>>>>>")
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap=1
        if swap == 0:
            break

arr=[5,4,3,2,1]
bubble_sort(arr)
print(arr)
