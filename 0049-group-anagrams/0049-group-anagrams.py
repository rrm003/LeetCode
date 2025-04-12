class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for s in strs:
            chars = sorted(s)
            sorted_s = "".join(chars)
            # print(sorted_s)
            if sorted_s not in lookup:
                lookup[sorted_s] = []

            lookup[sorted_s].append(s)
        
        grouped = []

        for key, val in lookup.items():
            grouped.append(val)

        return grouped