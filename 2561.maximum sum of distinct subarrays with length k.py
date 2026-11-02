class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = {}                # element -> window mein kitni baar
        curr_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            # naya element jodo
            curr_sum = curr_sum + nums[i]
            count[nums[i]] = count.get(nums[i], 0) + 1

            # window size k se bada ho gaya toh purana hatao
            if i >= k:
                old = nums[i - k]
                curr_sum = curr_sum - old
                count[old] = count[old] - 1
                if count[old] == 0:
                    del count[old]

            # window poori hai (i >= k-1) aur saare distinct hain
            if i >= k - 1 and len(count) == k:
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum
