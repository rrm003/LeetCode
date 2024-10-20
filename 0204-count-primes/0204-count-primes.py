class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        primes = [i % 2 for i in range(n+2)]
        primes[1] = 0
        
        i = 2
        while i < n+2:
            if i == 2:
                primes[i] = 1
                i+=1
                continue

            if primes[i] == 0: 
                i+=1
                continue

            multiplier = 2
            while i * multiplier < n+2:
                primes[i*multiplier] = 0
                multiplier += 1
            
            i+=1
        # print(primes)
        return sum(primes[:n])