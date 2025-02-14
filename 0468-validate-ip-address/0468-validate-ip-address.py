class Solution:
    def validateIPV4Fragment(self, fragment :str) -> bool:
        if len(fragment) < 1: return False
        if fragment[0] == "0": 
            if len(fragment) == 1: return True
            return False
        
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for x in fragment:
            if x not in valid: return False
        
        return int(fragment) > 0 and int(fragment) <= 255

    def validateIPV6Fragment(self, fragment :str) -> bool:
        if len(fragment) < 1 or len(fragment) > 4: return False
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

        for x in fragment:
            if x not in valid: return False
        
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP) == 0: return "Neither"
        
        ipv4 = queryIP.split(".")
        if len(ipv4) == 4:
            for fragemnt in ipv4:
                rslt = self.validateIPV4Fragment(fragemnt)
                if not rslt: break

            if rslt: return "IPv4"  

        ipv6 = queryIP.split(":")
        if len(ipv6) == 8:
            for fragemnt in ipv6:
                rslt = self.validateIPV6Fragment(fragemnt)
                if not rslt: break

            if rslt: return "IPv6"
        
        return "Neither"