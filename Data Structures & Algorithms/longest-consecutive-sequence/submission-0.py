class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_count=0 
        current_count=1  

        if len(nums)==0: 
            return(0)
        
        num=sorted(list(set(nums)))
        #print(num)
        for i in range(len(num)-1): 
            if num[i]==num[i+1]-1: 
                current_count+=1 
            else: 
                if current_count>longest_count: 
                    longest_count=current_count
                    current_count=1 
                else: 
                    current_count=1 
        return(max(longest_count, current_count))