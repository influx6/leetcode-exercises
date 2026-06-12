from typing import List

# product of array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []

        # we now we have the prefix sum
        for index in range(len(nums)):
            # skip 0, since we set value in prefix product
            if index == 0:
                prefix_product.append(1)
                continue
            prefix_product.append(prefix_product[index-1] * nums[index-1])

        # by default the ending of the array
        suffix_product = 1

        # loop in reverse so we can do suffix product,
        # python does not support index-- or index++ in
        # for loops, so use range(num, -1, -1)
        # where:
        #   num = is the count to start from
        #   -1 is the value to increment
        #   -1 is the exclusive final value to stop at
        #
        for last_index in range(len(nums)-1, -1, -1):
            prefix_product[last_index] = prefix_product[last_index] * suffix_product
            suffix_product = suffix_product * nums[last_index]

        print("ProductExceptSelf: items: ", nums, " is now: ", prefix_product)
        return prefix_product

Solution().productExceptSelf([1,2,3,4])
