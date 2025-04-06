class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # total_queens = 0
        visited = set()
        visited_cols = set()
        queen_positions = set()
        res = []

        def in_bounds(i: int, j: int) -> bool:
            return i >= 0 and i < n and j >= 0 and j < n

        def can_place(i: int, j: int) -> bool:
            # check top right
            r, c = i-1, j+1
            while in_bounds(r, c):
                if (r, c) in queen_positions:
                    return False
                r -= 1
                c += 1
                
            # check top left
            r, c = i-1, j-1
            while in_bounds(r, c):
                if (r, c) in queen_positions:
                    return False
                r -= 1
                c -= 1

            # check bottom right
            r, c = i+1, j+1
            while in_bounds(r, c):
                if (r, c) in queen_positions:
                    return False
                r += 1
                c += 1
                
            # check bottom left
            r, c = i-1, j-1
            while in_bounds(r, c):
                if (r, c) in queen_positions:
                    return False
                r -= 1
                c -= 1

            return True
        
        def dfs(i: int, queen_count: int, board: list) -> None:
            string = []

            for j in range(n):
                string.append(".")

            for j in range(n):
                if j in visited_cols:
                    continue

                if not can_place(i, j):
                    continue

                # place queen
                queen_positions.add((i, j))
                string[j] = "Q"
                board.append("".join(string))
                if queen_count == n - 1:
                    if (i, j) in queen_positions:
                        queen_positions.remove((i, j))
                    # visited_cols.remove(j)
                    res.append(board.copy())
                    board.pop()
                    return True

                visited_cols.add(j)
                
                dfs(i+1, queen_count + 1, board)
                board.pop()
                string[j] = "."

                if (i, j) in queen_positions:
                    queen_positions.remove((i, j))
                if j in visited_cols:
                    visited_cols.remove(j)
            return


        dfs(0, 0, [])

        return res