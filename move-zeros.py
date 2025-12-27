from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = b = 0
        print("Start: ", nums)
        while b < len(nums):
            value = nums[b]
            if value != 0:
                if a != b:
                    nums[a], nums[b] = nums[b], nums[a]
                a += 1
            b += 1
        print("End: ", nums)

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        a = 0
        print("Start: ", nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a += 1
        print("End: ", nums)

solution = Solution()
solution.moveZeroes([0])
solution.moveZeroes([0,1,0,3,12])
solution.moveZeroes([0, 0, 1,0,3,12])


solution2 = Solution2()
solution2.moveZeroes([0])
solution2.moveZeroes([0,1,0,3,12])
solution2.moveZeroes([0, 0, 1,0,3,12])
