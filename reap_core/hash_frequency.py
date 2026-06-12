## 3. Hash Map Frequency & Tracking
# This type of problem evaluates your ability to clean up tracking states and perform lookups rapidly, which is foundational for working with ledger or ledger-like data structures.
# ## Problem Statement
# Given an integer array nums and an integer k, return True if there are two distinct indices i and j in the array such that nums[i] == nums[j] and the absolute difference between i and j is at most k.
# ## Code Implementation


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    # Tracks the most recent index seen for each number
    seen_map = {}

    for i, num in enumerate(nums):
        if num in seen_map and i - seen_map[num] <= k:
            return True
        # Always update to the latest index to minimize future differences
        seen_map[num] = i

    return False


## Complexity Analysis

# * Time Complexity: $\mathcal{O}(N)$. The array is iterated over a single time, completing constant time hash table evaluations.
# * Space Complexity: $\mathcal{O}(N)$. The hash map scales linearly with the number of unique elements encountered.
