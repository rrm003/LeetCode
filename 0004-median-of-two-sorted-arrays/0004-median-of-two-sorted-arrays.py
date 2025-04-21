import heapq as hq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left  = []
        right = []
        
        m = len(nums1)
        n = len(nums2)

        i = 0 
        j = 0 

        while i < m or j < n:
            curr = 0
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    curr = nums1[i] 
                    i+=1
                else:
                    curr = nums2[j]
                    j+=1
            elif i < m:
                curr = nums1[i]
                i+=1
            elif j < n:
                curr = nums2[j]
                j+=1

            hq.heappush(left, -curr)
            max_left = -hq.heappop(left)
            hq.heappush(right, max_left)
            if len(right) >= len(left) + 1:
                min_right = hq.heappop(right)
                hq.heappush(left, -min_right)
        
        # print(left, right)
        if (m+n) % 2 == 0:
            m1 = -hq.heappop(left)
            m2 = hq.heappop(right)
            return (m1 + m2) / 2

        return -hq.heappop(left)