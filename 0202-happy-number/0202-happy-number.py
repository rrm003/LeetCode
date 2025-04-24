class Solution:
    def digitSquareSum(self, number):
        sum = 0

        while number:
            digit = number % 10
            number = number // 10

            sum += digit * digit
        
        return sum

    def isHappy(self, n: int) -> bool:
        
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)
            n = self.digitSquareSum(n)
            
        return True