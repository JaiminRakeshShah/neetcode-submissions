class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: 
        row=[]
        col=[]   
        nat=collections.defaultdict() 
        m=len(matrix) 
        n=len(matrix[0])

        for r in range(m): 
            for c in range(n): 
                if (matrix[r][c]==0): 
                    row.append(r)
                    col.append(c)
        
        for ro in row: 
            for co in range(n): 
                matrix[ro][co]=0 
        
        for co in col: 
            for ro in range(m): 
                matrix[ro][co]=0
                



        
        