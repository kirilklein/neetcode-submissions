class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        # at each step we record the index of the difference nums ones - num zeros
        # then we want to balance, we check whether we can balance and record the length
        zeros, ones = 0, 0
        max_length = 0
        for i, n in enumerate(nums):
            if n==0:
                zeros+=1
            else:
                ones+=1

            diff = ones - zeros
            if diff == 0:
                max_length = i+1
            else:
                if diff not in dic:
                    dic[diff] =  i
                else:
                    max_length = max(max_length, i - dic[diff])

        return max_length
