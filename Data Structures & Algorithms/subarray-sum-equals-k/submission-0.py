class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        dic = {0: 1}
        for x in nums:
            prefix += x
            diff = prefix - k
            count += dic.get(diff, 0)
            dic[prefix] = dic.get(prefix, 0) + 1
        
        return count


         

