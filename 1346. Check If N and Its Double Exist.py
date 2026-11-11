class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Check if there exist two indices i and j such that:
        - i != j
        - arr[i] == 2 * arr[j] (i.e., one element is double of another)

        Args:
            arr: List of integers to check

        Returns:
            bool: True if such pair exists, False otherwise
        """
        # Set to store elements we've seen so far
        seen_numbers = set()

        # Iterate through each element in the array
        for current_num in arr:
            # Check if double of current number exists in seen numbers
            # OR if current number is even and its half exists in seen numbers
            if (current_num * 2 in seen_numbers or
                (current_num % 2 == 0 and current_num // 2 in seen_numbers)):
                return True

            # Add current number to the set of seen numbers
            seen_numbers.add(current_num)

        # No valid pair found
        return False
