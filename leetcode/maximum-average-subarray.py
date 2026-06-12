from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[0:k])
        max_sum = window_sum

        # now moving from the index from k to the end, start is k
        for index in range(k, len(nums)):
            # remove the previous index i.e i - k (because i is now greater than k)
            # we are starting at K + 1 right, so to get the first index in the
            # last window, we do: current_index - k
            # With k = 4
            #
            # index = 4
            # Last Index to be removed is = index - k = 4 - 4 = 0
            #
            # index = 5
            # Last Index to be removed is = index - k = 5 - 4 = 1
            window_sum = window_sum + nums[index] - nums[index - k]
            if window_sum > max_sum:
                max_sum = window_sum

        print("MaxAvg of ", nums, " is: ", max_sum / k)
        return max_sum / k


solution = Solution()
assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75000
assert solution.findMaxAverage([5], 1) == 5.0000
assert solution.findMaxAverage([5, 0], 1) == 5.0000
assert solution.findMaxAverage([5, 0, 0, 0, 0], 1) == 5.0000
assert solution.findMaxAverage([1, 12, 5, 6, 50, 3], 4) == 18.25
assert solution.findMaxAverage([1, 12, 5, 6, 3, 50], 4) == 16
