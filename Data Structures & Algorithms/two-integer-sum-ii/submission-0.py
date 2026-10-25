class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = [target - n for n in numbers]
        pointer_min = 0
        pointer_max = len(numbers) - 1
        while (numbers[pointer_min] + numbers[pointer_max]) != target:
            sum_ = numbers[pointer_min] + numbers[pointer_max]
            if sum_<target:
                pointer_min+=1
            elif sum_>target:
                pointer_max-=1
            else:
                return [pointer_min+1, pointer_max+1]
        return [pointer_min+1, pointer_max+1]
