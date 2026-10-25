import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = s.lower()
        middle_index = len(s) // 2
        print("middle_index", middle_index)
        for i in range(middle_index):
            if s[i] != s[-i-1]:
                print(s[i], s[-i-1])
                return False
        return True