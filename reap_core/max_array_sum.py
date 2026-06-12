# Given an array of integers nums and an integer target, find the maximum length of a contiguous subarray that sums to exactly target. If no such subarray exists, return $0$.


def max_sub_array_len(nums: list[int], target: int) -> int:
    # Maps prefix_sum -> earliest index encountered
    prefix_map = {0: -1}
    current_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        current_sum += num

        # Check if a complement exists that yields the target sum
        complement = current_sum - target
        if complement in prefix_map:
            max_length = max(max_length, i - prefix_map[complement])

        # Only record the earliest index to maximize the subarray length
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length


## Complexity Analysis
#
# * Time Complexity: $\mathcal{O}(N)$. We traverse the array exactly once, performing $\mathcal{O}(1)$ dictionary lookups at each step.
# * Space Complexity: $\mathcal{O}(N)$. In the worst-case scenario, every prefix sum is unique and stored in the hash map.
