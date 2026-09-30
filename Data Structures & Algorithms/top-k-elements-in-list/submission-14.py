import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        dictt = {} 
        for num in nums: 
            if num in dictt: 
                dictt[num] += 1  # Fixed: Increment by 1
            else: 
                dictt[num] = 1  
                
        heapp = []
        for current_num, current_freq in dictt.items():  
            # Fixed: Put frequency first so the heap sorts by it
            to_add = (current_freq, current_num)
            heapq.heappush(heapp, to_add) 
            
            if len(heapp) > k: 
                heapq.heappop(heapp) 
                
        final = []
        # Fixed: Unpack matching the new (frequency, number) tuple structure
        for frequency, num in heapp: 
            final.append(num) 
            
        return final