class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        invalid = {0, -1}
        inf = 2**31 - 1

        def in_range(i: int, j: int) -> bool:
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(i: int, j: int) -> int:
            if not in_range(i, j) or grid[i][j] == -1 or (i, j) in visited:
                return inf

            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            res = inf

            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res = min(res, 1 + dfs(i + dx, j + dy))

            visited.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in invalid:
                    grid[i][j] = dfs(i, j)