from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k

solution = Solution()
assert abs(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) - 12.75000) < 1e-5
assert abs(solution.findMaxAverage([5], 1) - 5.0000) < 1e-5
assert abs(solution.findMaxAverage([5, 0], 1) - 5.0000) < 1e-5
assert abs(solution.findMaxAverage([5, 0, 0, 0, 0], 1) - 5.0000) < 1e-5
assert abs(solution.findMaxAverage([1, 12, 5, 6, 50, 3], 4) - 18.25) < 1e-5
assert abs(solution.findMaxAverage([1, 12, 5, 6, 3, 50], 4) - 16) < 1e-5