class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <=1:
            return True

        intervals.sort(key=lambda x: (x[0], x[1]))

        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[1] > interval[0]:
                return False
            prev = interval

        return True