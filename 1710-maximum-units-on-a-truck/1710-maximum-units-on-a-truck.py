class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        rem_size = truckSize

        boxTypes.sort(key=lambda x:(-x[1]))

        for box in boxTypes:
            b, u = box[0], box[1]
            if b >= rem_size:
                units += rem_size * u
                break
            else:
                units += b * u
                rem_size -= b
            
        return units