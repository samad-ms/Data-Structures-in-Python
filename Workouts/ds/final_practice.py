nums=[0,1,1,3,3]
k=4
maxsub=nums[0]
cursum=0
for i in range(len(nums)):
    print(i, k + i)
    cursum=sum(nums[i:k+i])

    maxsub=max(maxsub,cursum)
print(maxsub/4)