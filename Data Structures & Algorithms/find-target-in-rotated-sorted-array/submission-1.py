class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_dict={value:i for i, value in enumerate(nums)} 
        if target in nums_dict: 
            return(nums_dict[target])  
        else: 
            return(-1)

        