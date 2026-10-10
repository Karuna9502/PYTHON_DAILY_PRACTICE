class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i++
            elif not s[j].isalnum():
                j--
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i++
                j-- 

        return True
