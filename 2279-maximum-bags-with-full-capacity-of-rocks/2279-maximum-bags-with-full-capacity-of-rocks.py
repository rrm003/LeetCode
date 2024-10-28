class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rem = [x[0] - x[1] for x in zip(capacity, rocks)]
        rem.sort()

        have = additionalRocks
        count = 0
        for x in rem:
            if have <= 0: break
            have -= x
            if have >=0:
                count+=1

        return count