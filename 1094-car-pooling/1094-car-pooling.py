class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x : (x[1], x[2], x[0]))
        start = trips[0][1]
        stop = trips[-1][2]

        # print(trips)
        pickups = {}
        drops = {}
        for trip in trips:
            if trip[1] not in pickups:
                pickups[trip[1]] = 0

            pickups[trip[1]] += trip[0]

            if trip[2] not in drops:
                drops[trip[2]] = 0
                
            drops[trip[2]] += trip[0]

        # print(f"start {start}, stop {stop}")
        # print(f"pickups {pickups}")
        # print(f"drops {drops}")

        for pos in range(start, stop + 1):
            if capacity < 0 : return False

            if pos not in pickups and pos not in drops: continue

            if pos in drops:               
                capacity += drops[pos]
            
            if pos in pickups:
                capacity -= pickups[pos]

        return capacity >= 0