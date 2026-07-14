

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first window
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        # Initialize max_sum with the first window's sum
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum

        # Return the maximum average
        return max_sum / k
