class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        isMultiline = False
        isOneline = False

        source_str = "\\n".join(source)
        print(source_str)

        i = 0
        rslt = ""
        while i < len(source_str):
            print(i)
            if i+1 < len(source_str):
                # print(source_str[i:i+2])
                if source_str[i:i+2] == "/*" and not isOneline and not isMultiline:
                    isMultiline = True
                    i+=2
                    continue
                
                elif source_str[i:i+2] == "*/" and isMultiline:
                    isMultiline = False
                    i+=2
                    continue
                
                elif source_str[i:i+2] == "//" and not isMultiline:
                    isOneline = True
                    i+=2
                    continue
                
                elif source_str[i:i+2] == "\\n" and isOneline:
                    rslt+="\\n"
                    isOneline = False
                    i+=2
                    continue
            
            if isMultiline:
                i+=1
                continue
            
            if isOneline:
                i+=1
                continue
            
            rslt += source_str[i]
            i+=1
        
        print("rslt", rslt)
        splitted_rslt = rslt.split("\\n")
        splitted_rslt = [x for x in splitted_rslt if len(x) > 0 ]
        return splitted_rslt