from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        max_len = left = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        # at this point, the assumption is we are counting the 0 as 1,
        # so we need to remove the 0 from the max_len
        max_len -= 1
        # print("SubArray: ", nums, " | max_len: ", max_len)
        return max_len


instance = Solution()
instance.longestSubarray([1, 1, 1])
instance.longestSubarray([1, 0, 0])
instance.longestSubarray([0, 0, 1])
instance.longestSubarray([0, 0, 0, 0])
instance.longestSubarray([1, 1, 0, 1])
instance.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
