import sys
from heapq import heappush as hpush , heappop as hpop
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1 , 0)]
        dist = [[sys.maxsize]* cols for _ in range(rows)]
        dist[0][0] = 0
        minheap = []
        visited = set()
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1 

        hpush(minheap, (0, 0, 0))
        visited.add((0, 0))

        while minheap:
            timer, x, y = hpop(minheap)

            if x == (rows - 1) and y == (cols - 1):
                return timer 

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx <rows and 0<= ny < cols and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_time = timer + 1
                    if new_time  >= grid[nx][ny]:
                        hpush(minheap, (new_time, nx, ny))
                    else:
                        diff = grid[nx][ny] - new_time
                        new_time += diff
                        if diff % 2 == 0:
                            hpush(minheap,(new_time , nx, ny))
                        else:
                            hpush(minheap, (new_time + 1, nx, ny))

                    
        return -1





        