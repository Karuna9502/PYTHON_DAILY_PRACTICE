class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            digits = 0 
            n = num
            while n > 0:
                n = n // 10 
                digits = digits + 1
            if digits % 2 == 0:
                count = count + 1
        return count
