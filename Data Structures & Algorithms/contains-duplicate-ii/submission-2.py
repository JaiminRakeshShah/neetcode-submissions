class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]: 
                    if abs(i-j) <= k: 
                        return True
                    # Let it keep looping if abs(i-j) > k; do NOT return False here
        
        # If we finish checking every pair and find nothing, then return False
        return False