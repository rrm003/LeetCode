class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digi_logs = []     

        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for word in logs:
            words = word.split(" ")
            log = " ".join(words[1:])
            if log[0] in digits:
                digi_logs.append((log, words[0]))
            else:
                letter_logs.append((log, words[0]))

        letter_logs.sort(key=lambda x: (x[0], x[1]) )

        rslt = []

        for log in letter_logs:
            rslt.append(log[1] + " " + log[0])
        
        for log in digi_logs:
            rslt.append(log[1] + " " + log[0])

        return rslt