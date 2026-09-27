class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        ad={} 
        for strr in strs:
            strr_sorted = "".join(sorted(strr.lower())) 
            if strr_sorted not in ad:
                ad[strr_sorted]=[strr]  
            else: 
                ad[strr_sorted].append(strr) 
        return list(ad.values())
                




            

        


        