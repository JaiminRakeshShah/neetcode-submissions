import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        mul=math.prod(nums) 
        a=[]
        for i in range(len(nums)): 
            if nums[i] !=0:
                a.append(int(mul/nums[i]))  
            else: 
                lst=nums[:i] + nums[i+1:]
                muls=math.prod(lst)
                a.append(muls)
        return(a)



        