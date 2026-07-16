int minSubArrayLen(int target, int* nums, int numsSize) {
    int left = 0;
    int sum = 0;
    int minLength = numsSize + 1;

    for (int right = 0; right < numsSize; right++) {

        // Expand the window
        sum += nums[right];

        // Shrink the window while sum is enough
        while (sum >= target) {

            int currentLength = right - left + 1;

            if (currentLength < minLength) {
                minLength = currentLength;
            }

            sum -= nums[left];
            left++;
        }
    }

    if (minLength == numsSize + 1)
        return 0;

    return minLength;
}
