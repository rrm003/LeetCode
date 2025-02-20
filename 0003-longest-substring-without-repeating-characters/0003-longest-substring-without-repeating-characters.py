class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        rslt = 0
        while end < len(s):
            # print(start, end, s[start:end])
            if s[end] not in s[start:end]:
                end+=1
            else:
                rslt = max(rslt, end - start)
                start += 1
        rslt = max(rslt, end-start)
        return rslt