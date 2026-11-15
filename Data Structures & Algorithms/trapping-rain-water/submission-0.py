class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = self.get_max_l(height)
        max_r = self.get_max_r(height)

        res = 0
        for i in range(1, len(height)-1):
            diff = min(max_l[i], max_r[i]) - height[i]
            if diff>0:
                res += diff 

        return res

    def get_max_l(self, height):
        max_l = [0] * len(height)
        cmax = 0
        for i in range(1, len(height)):
            cmax = max(cmax, height[i-1])
            max_l[i] = cmax
        return max_l

    def get_max_r(self, height):
        height = height[::-1]
        max_l = self.get_max_l(height)
        return max_l[::-1]
