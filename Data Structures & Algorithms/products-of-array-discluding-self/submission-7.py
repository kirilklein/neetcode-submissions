class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive multiply all and divide
        results = len(nums)*[0]
        zero_counter = 0
        mult = 1
        for i, n in enumerate(nums):
            if zero_counter >=2:
                break
                
            if n == 0:
                zero_pos = i
                zero_counter += 1
                continue 
            mult *= n
        if zero_counter == 1:
            results[zero_pos] = mult
            return results
        if zero_counter>=2:
            return results
        print(zero_counter)
        return [int(mult/n) for n in nums]