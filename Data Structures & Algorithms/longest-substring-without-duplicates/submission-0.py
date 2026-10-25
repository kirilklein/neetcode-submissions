class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        seen=set()
        max_len = 0
        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                max_len=max(right-left, max_len)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
        return max_len        
            

        