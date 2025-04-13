# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if self.helper(i, n):
                return i
        return -1

    def helper(self, candidate, n):
        
        for i in range(n):
            if i == candidate: continue
            if knows(candidate, i) or not knows(i, candidate):
                return False
        
        return True
        