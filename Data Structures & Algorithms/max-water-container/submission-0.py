class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a=0 
        curr_a=0 
        left=0 
        right=len(heights)-1 
        while right>left: 
            width=right-left 
            h=min(heights[right], heights[left]) 
            curr_a= h*width 
            if curr_a>max_a: 
                max_a=curr_a  
            if heights[right]>heights[left]: 
                left+=1 
            else: 
                right-=1 
        return(max(max_a,curr_a))

        