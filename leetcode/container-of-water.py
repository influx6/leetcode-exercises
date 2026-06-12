from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            width = j - i
            h = min(height[i], height[j])
            max_area = max(max_area, width * h)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


solution = Solution()
print("maxArea: ", solution.maxArea([1,8,6,2,5,4,8,3,7]))
