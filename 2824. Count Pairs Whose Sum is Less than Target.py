class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
       
        nums.sort()

    
        count = 0

        
        for j, num_j in enumerate(nums):
            # Find the rightmost position where nums[i] < target - nums[j]
            # This gives us the count of valid first elements for current second element
            # We search only up to index j to avoid counting pairs twice and ensure i < j
            left_bound = bisect_left(nums, target - num_j, hi=j)

            
            count += left_bound

        return count
