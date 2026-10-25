class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {v:j for j,v in enumerate(nums)}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dic:
                j = dic[difference]
                if j!=i:
                    return [i, j] if i<j else [j,i]