def pivot_place(a,first,last):
    p=a[first]
    l=first+1
    r=last
    while True:
        while l <= r and a[l] < p:
            l += 1
        while l <= r and a[r]>p:
            r -= 1
        if l > r:
            break
        else:
            a[r],a[l]=a[l],a[r]
    a[first], a[r] = a[r], a[first]
    return r

def quick_sort(a,first,last):
    if first<last:
        p=pivot_place(a,first,last)
        quick_sort(a,first,p-1)
        quick_sort(a,p+1,last)

a=[5,4,3,2,1]

quick_sort(a,0,len(a)-1)

