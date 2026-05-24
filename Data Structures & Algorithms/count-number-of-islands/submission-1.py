class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        queue = []
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def isValid(i,j):
            return i >= 0 and j>=0 and i < ROWS and j < COLS
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in visited:
                    continue
                if grid[i][j] == "1":
                    islands+=1
                    queue.append((i,j))
                    while queue:
                        neighbor = queue.pop(0)
                        visited.add(neighbor)
                        l, m = neighbor
                        possibleNeighbors = [(l+1,m),(l,m+1),(l-1,m),(l,m-1)]
                        if grid[l][m] == "1":
                            for neighbor in possibleNeighbors:
                                if isValid(neighbor[0], neighbor[1]) and neighbor not in visited:
                                    queue.append(neighbor)
        return islands