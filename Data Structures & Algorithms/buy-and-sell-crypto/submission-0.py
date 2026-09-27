class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0 
        a=len(prices)
        for i in range(a): 
            for j in range(i+1,a): 
                profit=prices[j]-prices[i] 
                if profit>max_p: 
                    max_p=profit 
        return max_p
        