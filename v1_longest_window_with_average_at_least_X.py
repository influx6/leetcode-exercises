from typing import List

def longest_subarray_with_avg_at_least_X(nums: List[int], X: float) -> int:
    n = len(nums)

    def check(L: int) -> bool:
        """Return True if there is any window of length L with avg ≥ X."""
        # We'll subtract X from every element. Now we want sum(window) >= 0 for some window of length L.
        transformed = [num - X for num in nums]
        # Compute prefix sum
        prefix = [0]
        for val in transformed:
            prefix.append(prefix[-1] + val)

        min_prefix = 0
        for i in range(L, n + 1):
            # The window sum is prefix[i] - prefix[i-L]
            if prefix[i] - min_prefix >= 0:
                return True
            min_prefix = min(min_prefix, prefix[i - L + 1])
        return False

    low, high = 1, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1  # try longer
        else:
            high = mid - 1  # try shorter

    return ans

# Example usage:
nums = [1, 12, -5, -6, 50, 3]
X = 4
print("Longest subarray length with avg ≥", X, ":", longest_subarray_with_avg_at_least_X(nums, X))