class Solution:
    def isPalindrome(self, s: str) -> bool:
        all='abcdefghijklmnopqrstuvwxyz1234567890'
        all_list=list(all)
        s=s.lower() 
        s_l=list(s) 
        s_p=[] 
        for i in range(len(s_l)): 
            if s_l[i] in all_list:  
                s_p.append(s_l[i]) 
        return(s_p==s_p[::-1])

        