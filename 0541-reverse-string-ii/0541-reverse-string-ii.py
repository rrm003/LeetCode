class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        input = list(s)
        i = 0
        while i <= max(0, len(input)):
            a = i
            j = min(i + k - 1, len(input)-1)
            print(i, j)
            while i < j:
                input[i], input[j] = input[j], input[i]
                i += 1
                j -= 1
            
            i = a + 2*k 

        return "".join(input)