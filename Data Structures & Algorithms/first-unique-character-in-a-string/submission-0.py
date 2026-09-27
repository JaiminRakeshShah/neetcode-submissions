class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list=list(s) 
        s_dict={}
        for char in s_list:  
            if char in s_dict: 
                s_dict[char]+=1 
            else: 
                s_dict[char]=1 
        for i, char in enumerate(s): 
            if s_dict[char]==1: 
                return i 
        return -1
        
        

                