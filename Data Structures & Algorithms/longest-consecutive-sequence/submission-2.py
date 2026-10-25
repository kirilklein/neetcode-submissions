class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums)==0:
            return 0
        previous = nums[0]
        l = 1
        max_l = l
        for n in nums:
            diff = n-previous
            if diff==0:
                continue
            if diff>1:
                l = 1
            else:
                l+=1
            if l>max_l:
                max_l = l
            previous = n

        return max_l  