class Solution:
    def reverseBits(self, n: int) -> int:
        bin = ""

        while n > 0:
            bin += str(n % 2)
            n //= 2

        while len(bin) < 32:        
            bin = bin + "0" 

        m = 1
        rslt = 0
        for x in bin[::-1]:
            rslt += int(x) * m 
            m *= 2

        return rslt
