def averageValue(a):
    """
    :type nums: List[int]
    :rtype: int
    """
    l=count=sum=0
    r=len(a)-1
    for i in range(len(a)//2):
        if l<r:
            if a[l]%6==0:
                sum=sum+a[l]
                count=count+1
            if a[r]%6==0:
                sum=sum+a[r]
                count=count+1
            l+=1
            r-=1
    if count>0:
        return sum/count
    else:
        return 0

nums=[1,3,6,10,12,15]
print(averageValue(nums))