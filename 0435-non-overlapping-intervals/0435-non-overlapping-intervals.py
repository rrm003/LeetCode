class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1]))
        nonoverlapping = []
        # print("Sorted Intervals", intervals)
        nonoverlapping.append(intervals[0])

        i = 1
        count = 0
        while i < len(intervals):
            prev = nonoverlapping[-1]
            curr = intervals[i]

            if curr[0] < prev[1]:
                # prev = min(curr[0], prev[0]), max(curr[1], prev[1])
                # nonoverlapping[-1] = prev
                count += 1
            else:
                nonoverlapping.append(curr)

            i+=1

        # print("Non Overlapping", nonoverlapping)
        return count