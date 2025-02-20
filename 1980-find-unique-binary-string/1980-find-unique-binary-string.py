class Solution:
    def combinations(self, i, l, bin, nums):
        if i == l: 
           if bin not in nums: return bin
           return ""

        rslt = self.combinations(i+1, l, bin + "0", nums)
        if rslt : return rslt
        rslt = self.combinations(i+1, l, bin + "1", nums)

        return rslt

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if not nums: return ""
        l = len(nums[0])

        rslt = self.combinations(0, l, "", nums)
        
        return rslt