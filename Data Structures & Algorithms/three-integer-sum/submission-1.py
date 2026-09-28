import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = set()
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    unique_triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                        
        # Convert the unique tuples back into lists for the final answer
        return [list(triplet) for triplet in unique_triplets]