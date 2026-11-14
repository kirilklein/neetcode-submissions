class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the only information we need is the min and max but in the righth order
        # because when we are at 1 for example. we only want to know whatis the minimum so far.
        # and then we compute the diff. if the diff is negative for all return 0
        # otherwise return the max diff
        min_so_far = prices[0]
        max_profit = 0
        for v in prices[1:]:
            max_profit = max(v-min_so_far, max_profit)
            min_so_far = min(v, min_so_far)

        return max_profit

