    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):

            # If character is already inside the current window
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            # Update the latest index of the character
            last_seen[s[right]] = right

            # Calculate current window length
            current_length = right - left + 1

            # Update maximum length
            max_length = max(max_length, current_length)

        return max_length
