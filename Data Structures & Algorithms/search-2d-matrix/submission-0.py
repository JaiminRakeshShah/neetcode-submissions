class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_dict={}
        for i, value in enumerate(matrix): 
            for j, val in enumerate(value):  
                num_dict[val]=(i,j)
        if target in num_dict: 
            return True 
        else: 
            return False

                





        