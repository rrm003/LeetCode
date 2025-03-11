class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in lookup:
                lookup[sorted_word] = []
            lookup[sorted_word].append(word)

        return list(lookup.values())