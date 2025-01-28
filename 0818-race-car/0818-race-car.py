class Solution:
    def racecar(self, target: int) -> int:
        queue = []
        visited = set()

        queue.append((0, 1, 0))
        

        while len(queue) > 0:
            pos, speed, dist = queue[0]
            queue = queue[1:]

            if pos == target: return dist

            if (pos, speed) in visited:
                continue
            
            visited.add((pos, speed))

            queue.append((pos + speed, speed * 2, dist + 1))

            if (pos+speed > target and speed>0) or (pos+speed < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append((pos, speed, dist + 1))

        return 0