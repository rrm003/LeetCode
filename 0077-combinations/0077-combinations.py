class Solution:
    def generate(self, candidates, i,  curr, k):
        if i >= len(candidates):
            # print(curr)
            if len(curr) == k:
                return [curr]
            return []

        rslt = []
        left = curr.copy()
        rslt.extend(self.generate(candidates, i+1, left, k))

        right = curr.copy()
        right.append(candidates[i])
        rslt.extend(self.generate(candidates, i+1, right, k))

        return rslt

    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]

        return self.generate(arr, 0, [], k)