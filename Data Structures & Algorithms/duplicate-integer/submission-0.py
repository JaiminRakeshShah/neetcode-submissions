from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        count_dict=Counter(nums) 
        return any(value > 1 for value in count_dict.values())
        