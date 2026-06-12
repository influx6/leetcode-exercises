from typing import List


# Solution1 is based on using two pointes, and the idea that if we sort the array
# we will have the list going from smallest to biggest which provides us a way to
# efficiently eliminate the need to do lots of checks:
#
# If the sum of the two values at the current two pointers is X
# and X is > than K, then we know other values below the largest which is the second pointer (since its sorted)
# will also be more than k, so we reduce pointer 2, to get a lesser/smaller second pointer.
#
# We do the same if sum is less than K, it means the left pointer (smaller values) is to small,
# so we increment it to get a bigger next value and try again.
#
# We increment the count only when we find a matching sum and increment left and decrement right
# when the is equal as well to find the other pairs.
#
# Though because of sorting, this is a time complexity of O(n log n) (sort) + O(n) iteration
# leading to a O(n log n + n) = O(2n log n) but really O(n log n) operation as it dominates.
#
# i.e O(n) = 1k but O(n log n) = 20k becaue log2(1k) approximately = 20, so 20 x 1k = 20k
class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a = 0
        b = len(nums) - 1
        count = 0

        nums.sort()

        while a < b:
            value_a = nums[a]
            value_b = nums[b]

            sum_a = value_b + value_a
            if sum_a == k:
                count += 1

            if sum_a > k:
                b -= 1
            elif sum_a < k:
                a += 1
            else:
                a += 1
                b -= 1

        print("Ops from: ", nums, " and k=", k, " is=", count)
        return count


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0

        frequencies = {}

        # first loop: build hashmap O(n)
        for value in nums:
            frequencies[value] = frequencies.get(value, 0) + 1

        # second loop: calculate ops (n)
        for value in nums:
            comp = k - value

            value_frequency = frequencies[value]

            # if we are equal to compliment then its
            # the same, total operation is frequency / 2
            # but we must remove equal total frequency from
            # hashmap cause it means we use up the whole in pairing
            if value == comp:
                count += value_frequency // 2
                frequencies[value] = frequencies[value] - value_frequency
                continue

            # if its not in frequencies, nothing to do here, move on.
            if comp not in frequencies:
                continue

            # if we are not then we can instead find which
            # use the lesser frequency cause thats how much pairing we can do
            # add it to count and decrement all by it
            selected_comp = min(frequencies[comp], value_frequency)
            count += selected_comp
            frequencies[value] = frequencies[value] - selected_comp
            frequencies[comp] = frequencies[comp] - selected_comp

        print("Ops from: ", nums, " and k=", k, " is=", count)
        return count


sol1 = Solution1()
print("Solution1: ")
print("Ops should be 2 but its: ", sol1.maxOperations([1, 2, 3, 4], 5))
print("Ops should be 2 but its: ", sol1.maxOperations([4, 1, 3, 2], 5))
print("Ops should be 1 but its: ", sol1.maxOperations([3, 3], 6))
print("Ops should be 0 but its: ", sol1.maxOperations([3], 6))

sol2 = Solution2()
print("Solution2: ")
print("Ops should be 2 but its: ", sol2.maxOperations([1, 2, 3, 4], 5))
print("Ops should be 2 but its: ", sol2.maxOperations([4, 1, 3, 2], 5))
print("Ops should be 1 but its: ", sol2.maxOperations([3, 3], 6))
print("Ops should be 0 but its: ", sol2.maxOperations([3], 6))
