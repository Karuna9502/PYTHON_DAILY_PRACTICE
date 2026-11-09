class Solution:
    def largest(self, arr):
        # code here
        max = float('-inf')
        for num in arr:
            if num > max:
                max = num 
        return max 
