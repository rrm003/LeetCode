class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # print(str1, len(str1))
        # print(str2, len(str2))

        smallest = str1 if len(str1) < len(str2) else str2
        longest = str1 if len(str1) >= len(str2) else str2
        
        # print("smallest: ", smallest, "longest: ", longest)
        for i in range(len(smallest)+1, 1 , -1):
            curr = smallest[:i]
            # print("curr: ", curr, "len: ", len(curr))
            if (len(smallest) % len(curr) == 0 and len(longest) % len(curr) == 0):
                srep = len(smallest) // len(curr)
                lrep = len(longest) // len(curr)

                snew = curr * srep
                lnew = curr * lrep
                # print("snew: ", snew, "slen: ", len(snew),  "lnew: ", lnew, "llen: ", len(lnew))
                if snew == smallest and lnew == longest:
                    print("found substring", curr)
                    return curr
            
        return ""
