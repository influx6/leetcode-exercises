from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for value in nums:
            if value <= first:
                first = value
            elif value <= second:
                second = value
            else:
                return True

        return False


solution = Solution()
print("Result: ", solution.increasingTriplet([2,1,5,0,4,6]))
print("Result: ", solution.increasingTriplet([5,4,3,2,1]))
print("Result: ", solution.increasingTriplet([1,2,3,4,5]))
