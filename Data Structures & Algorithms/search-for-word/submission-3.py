class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(i, j, string):
            if len(string) == 0:
                return True
            if i >= len(board) or j >= len(board[0]) or i <0 or j <0 or (i,j) in path:
                return False
            if board[i][j] == string[0]:
                path.add((i,j))
                res = dfs(i+1, j, string[1:]) or dfs(i, j+1, string[1:]) or dfs(i-1, j, string[1:]) or dfs(i,j-1, string[1:])
                path.remove((i,j))
                return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        return False
