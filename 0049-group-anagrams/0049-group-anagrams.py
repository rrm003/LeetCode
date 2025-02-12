class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for x in strs:
            y = x
            key = "".join(sorted(x))
            if key not in lookup:
                lookup[key] = []

            lookup[key].append(y)
        
        rslt = []
        for val in lookup.values():
            rslt.append(val)

        return rslt