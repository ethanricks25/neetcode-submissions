class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [1, 2, 3] -> [7, 4, 1] [ [ROWS-1][COL-3] , [ROWS-2][COL-3] , [ROWS-3][COL-3] ]
        # [4, 5, 6] -> [8, 5, 2] [ [ROWS-1][COL-2] , [ROWS-2][COL-2] , [ROWS-3][COL-2] ]
        # [7, 8, 9] -> [9, 6, 3] [ [ROWS-1][COL-1] , [ROWS-2][COL-1] , [ROWS-3][COL-1] ]

        N = len(matrix)
        for i in range(N // 2):
            for j in range(N):
                matrix[i][j], matrix[N-1-i][j]  = matrix[N-1-i][j], matrix[i][j]
        
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
                

