class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_pointer = 0
        high_pointer = 1
        if len(prices)<2:
            return 0
        lowest = prices[0]
        highest = prices[1]
        curr_diff = highest - lowest
        highest_diff = curr_diff if curr_diff > 0 else 0
        
        for i in range(1, len(prices)-1):
            high_pointer += 1
            if prices[i]<lowest:
                lowest = prices[i]
            curr_diff = prices[high_pointer]-lowest
            if curr_diff > highest_diff:
                highest_diff = curr_diff
        return highest_diff
            

        
        # for each day what is the cheapest i could baught at before today


