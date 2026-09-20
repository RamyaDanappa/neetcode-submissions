class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def get_neighbor(x,y):
            res =[]
            if x+1<len(grid):
                res.append((x+1,y))
            if x-1>=0:
                res.append((x-1,y))
            if y+1<len(grid[0]):
                res.append((x, y+1))
            if y-1>=0:
                res.append((x, y-1))
            return res

        def bfs(q):                        # CHANGED: takes the queue directly, not a single (r,c)
            fresh = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        fresh += 1

            if fresh == 0:
                return 0                    # CHANGED: 0 fresh oranges -> answer is 0, not -1

            minutes = 0
            while q:
                level_size = len(q)         # CHANGED: process one full layer = one minute
                rotted_this_round = False
                for _ in range(level_size):
                    r,c=q.popleft()
                    for NR,NC in get_neighbor(r,c):
                        if grid[NR][NC] ==1:
                            grid[NR][NC]=2
                            fresh -= 1
                            rotted_this_round = True
                            q.append((NR,NC))
                if rotted_this_round:
                    minutes += 1             # CHANGED: count minutes, not total rotted oranges

            return minutes if fresh == 0 else -1   # CHANGED: base -1 on leftover fresh, not on count

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))          # CHANGED: collect ALL rotten oranges first
        return bfs(q)                        # CHANGED: single call after seeding, not one per '2' found