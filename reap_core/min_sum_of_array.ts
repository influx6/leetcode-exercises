function min_sub_array(nums: Array<number>, target: number): number {
  let min_length = Infinity;
  let current_sum = 0;
  let left = 0;

  let right = 0;
  for (right = 0; right < nums.length; right++) {
    current_sum += nums[right];

    while (current_sum >= target) {
      min_length = Math.min(min_length, right - left + 1);
      current_sum -= nums[left];
      left += 1;
    }
  }

  console.log("Array: ", min_length, nums.slice(left, right));
  if (min_length == Infinity) return 0;
  return min_length;
}

console.log("minSubArray: ", min_sub_array([1, 2, 3, 4, 5], 3));

// Fintech platforms handle transactional timelines and data streaming. Sliding window algorithms are critical for optimizing these operations.
// ## Problem Statement
// Given an array of positive integers nums and a positive integer target, find the minimal length of a contiguous subarray for which the sum is greater than or equal to target. If there is no such subarray, return $0$ instead.
// ## Code Implementation

// def min_sub_array_len(target: int, nums: list[int]) -> int:
//     left = 0
//     current_sum = 0
//     min_length = float('inf')

//     for right in range(len(nums)):
//         current_sum += nums[right]

//         # Shrink the window from the left as long as the condition is met
//         while current_sum >= target:
//             min_length = min(min_length, right - left + 1)
//             current_sum -= nums[left]
//             left += 1

//     return min_length if min_length != float('inf') else 0
