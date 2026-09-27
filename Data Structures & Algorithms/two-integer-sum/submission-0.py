class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        

        for i, num in enumerate(nums): 
            competent=target-num 
            if competent in seen: 
                return[seen[competent],i] 
            seen[num]=i 
        
        
        