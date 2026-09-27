class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_d={}
        for char in s:  
            if char in s_d: 
                s_d[char]+=1 
            else: 
                s_d[char]=1 
        for i,c in enumerate(s): 
            if s_d[c]==1: 
                return i
            
        return(-1)



        