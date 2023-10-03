def majority(arr):
    count = {}
    res, maxcount = 0, 0

    for n in arr:
        count[n]=1+count.get(n,0)
        res=n if count[n]>maxcount else res
        maxcount=max(count[n],maxcount)
    print(count)

arr=[1,1,1,2,2,1,1,3]
majority(arr)
        #
        # candidate = None
        # count = 0
        #
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #         count = 1
        #     elif candidate == num:
        #         count += 1
        #     else:
        #         count -= 1
        #
        # return candidate
        #
