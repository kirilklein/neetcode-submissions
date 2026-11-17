from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, 4, 3, 2]
        # sum([ceil(n/k) for n in piles])
        # how to not recompute it for each h?
        # we need some sort of binary search
        # then its O(n * log(n))
        # base case k=1 -> max
        # for minimum time k=max(piles) -> min time
        # find something in the middle and check is it larger or smaller

        # start with mid = (max(piles) + 1)//2
        # if res > h:
        #  (mid + max(piles)) //2
        # else:
        # (1 + mid) //2
        # while
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.get_duration(piles, mid) <= h:
                r = mid
            else:
                l = mid + 1
            
        return l

    def get_duration(self, piles, k):
        return sum([ceil(n/k) for n in piles])