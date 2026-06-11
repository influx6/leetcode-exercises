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
