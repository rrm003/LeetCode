class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        if l <= 1: return l

        intervals.sort(key = lambda x : (x[0], x[1]))

        i = 0 
        max_rooms = 0
        while i < l - 1:
            rooms = 0
            curr = intervals[i]
            end = curr[1]

            while i < l - 1 and end > intervals[i][0]:
                i += 1
                rooms += 1
                end = max(end, intervals[i][1])

            max_rooms = max(max_rooms, rooms)
        
        return max_rooms

