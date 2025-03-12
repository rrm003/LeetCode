class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        number = 0

        i = 0
        while i < l :
            c = s[i]
            if c == "I":
                if i < len(s) - 1 and s[i+1] == "V":
                    number += 4
                    i+=1
                elif i < len(s) - 1 and s[i+1] == "X":
                    number += 9
                    i+=1
                else:
                    number += 1

            elif c == "V":
                # if i < len(s) - 1 and s[i+1] == "I":
                #     number += 6
                # else: 
                number += 5
                
            elif c == "X":
                if i<len(s) - 1 and s[i+1] == "L":
                    number += 40
                    i+=1
                elif  i<len(s) - 1 and s[i+1] == "C":
                    number += 90
                    i+=1
                else:
                    number += 10

            elif c == "L":
                number += 50

            elif c == "C":
                if i<len(s) - 1 and s[i+1] == "D":
                    number += 400
                    i += 1
                elif i<len(s) - 1 and s[i+1] == "M":
                    number += 900
                    i += 1
                else:
                    number += 100

            elif c == "D":
                number += 500

            elif c == "M":
                number += 1000

            i += 1
        
        return number
