from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        n = 0
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]


        def bfs(r,c):
            q = deque([[r,c]])
            grid[r][c] = "0"
            def check_and_flip(r,c):
                if 0<=r<rows and 0<=c<cols and grid[r][c]=="1":
                    grid[r][c] = "0"
                    q.append([r,c])



            while q:
                r, c = q.popleft()
                for d in directions:
                    nr, nc = r+d[0], c+d[1]
                    check_and_flip(nr,nc)




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    n+=1
                    bfs(r, c)

        return n
        