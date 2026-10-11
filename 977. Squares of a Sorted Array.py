class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        i, j = 0, len(nums) - 1
        while i <= j:
            left_squ = nums[i] * nums[i]
            right_squ = nums[j] * nums[j]
            if left_squ > right_squ:
                result.append(left_squ)
                i = i + 1
            else:
                result.append(right_squ)
                j = j - 1
        return result[::-1]
