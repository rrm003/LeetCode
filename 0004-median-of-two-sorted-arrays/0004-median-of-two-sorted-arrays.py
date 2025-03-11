class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        m = (l1 + l2) // 2 
        # 8 8 -> 8 & 7
        # 8 7 -> 7

        pt_list1 = 0
        pt_list2 = 0
        pt = 0
        f, s = 0, 0
        while pt <= m:
            if pt_list1 >= l1 or pt_list2 >= l2:
                if pt_list1 < l1:
                    f = s 
                    s = nums1[pt_list1] 
                    pt_list1 += 1
                elif pt_list2 < l2: 
                    f = s
                    s = nums2[pt_list2]
                    pt_list2 += 1
            elif nums1[pt_list1] <= nums2[pt_list2]:
                f = s
                s = nums1[pt_list1]
                pt_list1 += 1
            elif nums1[pt_list1] > nums2[pt_list2]:
                f = s 
                s = nums2[pt_list2]
                pt_list2 += 1
            
            pt+=1
        
        return s if (l1 + l2) % 2 else (f + s) / 2
# 1 1 3 3 4 4 5