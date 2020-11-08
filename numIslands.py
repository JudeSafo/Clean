#Author: Jude Safo

from typing import List
import numpy as np

class Islands:
        def __init__(self, grid: List[List[int]]):
                self.grid = grid
                self.n = len(grid)
                self.m = len(grid[0])
                self.path = 0
                self.largest_island = 0

        def dfs(self, i: int, j: int) -> int:
                grid  = self.grid
                m, n = self.m, self.n

                # end of path, return path
                if not grid:
                        return 0

                # initialize path and update count
                self.path = 0
                if 0 <= grid[i][j] <= m  and 0 <= grid[i][j] < n:
                        if grid[i][j] == '1':
                            grid[i][j] = '#'
                            self.path = sum(map(self.dfs, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                            return 1

                        if grid[i][j] == '#':
                                #TODO: what to do if you see an inner island
                                return 1

                return self.path

        def findLargest(self) -> int:
                n, m = self.n, self.m
                largest_island = 0

                # greedy search for largest path
                for i in range(n):
                        for j in range(m):
                                largest_island = max(self.dfs(i, j), largest_island)

                return largest_island

grid = [list(i) for i in np.random.randint(0,2, size = (4,4))]
print(grid, "\n", Islands(grid).findLargest())
