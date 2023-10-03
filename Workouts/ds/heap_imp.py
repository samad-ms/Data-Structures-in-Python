def lastStoneWeight(stones):
    stones.sort()
    while len(stones) > 1:
        diff = abs(stones[-1] - stones[-2])
        if diff == 0:
            stones.pop()
            stones.pop()
        else:
            stones.pop()
            stones.pop()
            stones.append(diff)
            stones.sort()
            print(stones)
    if len(stones) == 0:
        return 0
    else:
        return stones[0]

l1=[7,6,7,6,9]
print(lastStoneWeight(l1))
